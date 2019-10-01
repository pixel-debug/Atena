#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Main

# --------------------------------------------------------


import cv2
import time
import glob
#import HSV as hsv
import Tela as tela
import Motores as motor
import Variaveis as var
import RPi.GPIO as GPIO
import Sensores as sensor
import Tratamento as trata
import Interface as interface
from picamera import PiCamera
import Gerenciador as gerencia
import Configuracoes as definir
from picamera.array import PiRGBArray


frames = PiCamera()
frames.framerate = var.taxa_quadros
frames.resolution = (var.tam_original_tela_x, var.tam_original_tela_y)
capturaFrames = PiRGBArray(frames, size=(var.tam_original_tela_x, var.tam_original_tela_y))

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

ctr_vel_motor_esq, ctr_vel_motor_dir = GPIO.PWM(var.pin_ENB, 500), GPIO.PWM(var.pin_ENA, 500)
ctr_vel_motor_esq.start(0)
ctr_vel_motor_dir.start(0)

time.sleep(1)



inicializacao = False
autorizado = False
'''
while(inicializacao is False):
	opcao_destino = interface.menu_texto()	
	resposta_autorizacao, ck1, ck2, ck3 = trata.interface_menu(opcao_destino)
	inicializacao = resposta_autorizacao
'''


# 138 frames em 1 minuto
cont_frames = 0

class main:
	try:
		for frame in frames.capture_continuous(capturaFrames, format="bgr", use_video_port=True):
			
			#print(ck1, ck2, ck3)
			ck1, ck2, ck3 = False, False, False

			# --------------------------- Obtencao valores sensores --------------------------
			# Obtendo quadros capturados pela camera
			imagem = frame.array

			# Obtendo valores brutos dos fototransistores
			a0, a1, a2, a3, b0, b1, b2, b3 = sensor.fototransistores()

			# Obtendo valores brutos sensor de obstaculo 
			#distancia_obstaculo = sensor.vl530x()	
			# --------------------------------------------------------------------------------


			# --------------------------- Definindo Imagens Filhas ---------------------------
			imagem_pista = imagem.copy()

			imagem_sinalizacao_dir = imagem.copy()
			imagem_sinalizacao_esq = imagem.copy()

			imagem_obstaculo = imagem.copy()

			imagem_sinalizacao_dir = imagem_sinalizacao_dir[var.y1_img_sinalizacao_dir:var.y2_img_sinalizacao_dir, var.x1_img_sinalizacao_dir:var.x2_img_sinalizacao_dir]
			imagem_sinalizacao_esq = imagem_sinalizacao_esq[var.y1_img_sinalizacao_esq:var.y2_img_sinalizacao_esq, var.x1_img_sinalizacao_esq:var.x2_img_sinalizacao_esq]

			
			# --------------------- Obtentendo Respostas dos Tratamentos ---------------------
			# Deteccao das faixas na pista
			(
				imagem_perspectiva_pista,
				imagem_faixa_esq, 
	   			imagem_faixa_dir,
				status_visao_faixa_dir, 
				status_visao_faixa_esq,
				status_anormalidade_faixa_dir, 
				status_anormalidade_faixa_esq
			) = trata.deteccao_faixas_visao(imagem_pista)
			

			(
				status_a0, 
				status_a1, 
				status_a2, 
				status_a3, 
				status_b0, 
				status_b1, 
				status_b2, 
				status_b3
			) = trata.deteccao_faixas_fototransistores(a0, a1, a2, a3, b0, b1, b2, b3)

		
			# Deteccao de obstaculos na pista
			(
				imagem_obstaculos,
				status_obstaculo_visao, 
				status_obstaculo_vl53x, 
			) = trata.deteccao_obstaculo(imagem_obstaculo, 0)					
			
			status_obstaculo_vl53x = False

			
			# Deteccao de placas na pista
			(
				status_placa_pare, 
				status_placa_pedestre, 
				status_placa_desvio 
			) = trata.sinalizacao_direita(imagem_sinalizacao_dir)
			

			
			# Deteccao de checkpoints na pista
			(
				imagem_area_checkpoints,
				status_ck_1, 
				status_ck_2, 
				status_ck_3,
			) = trata.sinalizacao_esquerda(imagem_sinalizacao_esq)
			
			# --------------------------------------------------------------------------------
			

			'''
			# -------------------------- Condicionais Placas---------------------------------
			if(status_placa_pare is True):
				gerencia.placa_pare(ctr_vel_motor_dir, ctr_vel_motor_esq)
			elif(status_placa_pedestre is True):
				gerencia.placa_pedestre(ctr_vel_motor_dir, ctr_vel_motor_esq)
			elif(status_placa_desvio is True):
				gerencia.placa_desvio(ctr_vel_motor_dir, ctr_vel_motor_esq)
			'''					
					
			# -------------------------------------------------------------------------------

		
			# ------------------------ Condicionais Checkpoints -----------------------------
			if((ck1 is True) and (status_ck_1 is True)):
				print("Você chegou no destino {0}. Desligando...".format(var.nome_check_1))			
				break
			elif((ck2 is True) and (status_ck_2 is True)):  
				print("Você chegou no destino {0}. Desligando...".format(var.nome_check_2))
				break
			elif((ck3 is True) and (status_ck_3 is True)):
				print("Você chegou no destino {0}. Desligando...".format(var.nome_check_3))
				break

			# -------------------------------------------------------------------------------


			# ----------------------------- DEFININDO COMANDOS ------------------------------
			(
				MOVIMENTO_FRENTE,
				CORRECAO_MOTOR_DIR_VISAO,
				CORRECAO_MOTOR_ESQ_VISAO,
				DETECCAO_OBSTACULOS_VISAO,
			) = gerencia.definicao_de_comandos(status_a0, status_a1, status_a2, status_a3, status_b0, status_b1, status_b2, status_b3, status_visao_faixa_dir, status_visao_faixa_esq, status_obstaculo_vl53x)
			# -------------------------------------------------------------------------------
					

			# ------------------ *** Condicionais De Movimentacao *** -----------------------
			
			# Seguir em frente ou manter robô parado 	
			if(MOVIMENTO_FRENTE is True):
				print("Seguindo em frente...")
				gerencia.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)					
			

			# Correcao do motor da direita com Visao Comp 
			elif (CORRECAO_MOTOR_DIR_VISAO is True):
				while(CORRECAO_MOTOR_DIR_VISAO is not False):
					print("Virar Esquerda com Visao") 
					gerencia.correcao_motor_dir(var.velVisao, ctr_vel_motor_dir, ctr_vel_motor_esq)
					CORRECAO_MOTOR_DIR_VISAO = False					
		

			# Correcao do motor da esquerda com Visao Comp 
			elif (CORRECAO_MOTOR_ESQ_VISAO is True):
				while(CORRECAO_MOTOR_ESQ_VISAO is not False):
					print("Virar Direita com Visao")
					gerencia.correcao_motor_esq(var.velVisao, ctr_vel_motor_dir, ctr_vel_motor_esq)
					CORRECAO_MOTOR_ESQ_VISAO = False
			
		
			# Detccao faixa direita Fototransitor
			elif (status_a0 is True):
				while(status_a0 is not False):
					print("Virar Esquerda A0")
					a0, _, _, _, _, _, _, _ = sensor.fototransistores() 
					motor.movimento_esquerda(var.velEmergencia, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(a0 >= var.CONST_A0): 
						status_a0 = False

			elif (status_a1 is True):
				while(status_a1 is not False):
					print("Virar Esquerda A1")
					_, a1, _, _, _, _, _, _ = sensor.fototransistores() 
					motor.movimento_esquerda(var.velEmergencia, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(a1 >= var.CONST_A1): 
						status_a1 = False


			# Detccao faixa esquerda Fototransitor
			elif (status_b0 is True):
				while(status_b0 is not False):
					print("Virar Direita B0")
					_, _, _, _, b0, _, _, _ = sensor.fototransistores() 
					motor.movimento_direita(var.velEmergencia, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(b0 >= var.CONST_B0): 
						status_b0 = False

			elif (status_b1 is True):
				while(status_b1 is not False):
					print("Virar Direita B1")
					_, _, _, _, _, b1, _, _ = sensor.fototransistores() 
					motor.movimento_direita(var.velEmergencia, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(b1 >= var.CONST_B1): 
						status_b1 = False

	
			else:
				print("Anomalia, manter robô parado!")	
				motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
			# --------------------------------------------------------------------------------


			# -------------------------- Apresentacao Telas ---------------------------------
			tela.apresenta("Sinalizacoes da Esquerda", imagem_sinalizacao_esq, 80, 10)
			tela.apresenta("Imagem Original", imagem, 580, 10)
			tela.apresenta("Sinalizacoes da Direita", imagem_sinalizacao_dir, 1080, 10)
		
			tela.apresenta("Imagem Faixa Esquerda", imagem_faixa_esq, 80, 355)
			tela.apresenta("Imagem Perspetiva Pista", imagem_perspectiva_pista, 580, 355)
			tela.apresenta("Imagem Faixa Direita", imagem_faixa_dir, 1080, 355)

			tela.apresenta("Imagem obstaculos", imagem_obstaculos, 580, 705)

			# -------------------------------------------------------------------------------

			'''
			# ----------------- Apresentacao Telas Monitor Pequeno ---------------------------
			#cv2.imshow("Imagem Placas",imagem)
			tela.apresenta("Imagem Original", imagem, 10, 10)
			#tela.apresenta("Imagem Checkpoints", imagem_deteccao_checkpoints, 10, 10)
			#tela.apresenta("Imagem Placas", imagem_detecao_placa, 500, 10)
			#tela.apresenta("Imagem obstaculos", imagem_obstaculos, 500, 10)
			#tela.apresenta("Imagem Perspe", imagem_perspectiva_pista, 500, 10)
			#tela.apresenta("Imagem Faixa Esquerda", imagem_faixa_esq, 10, 400)
			#tela.apresenta("Imagem Faixa Direita", imagem_faixa_dir, 500, 400)
			# -------------------------------------------------------------------------------
			'''
			
			cv2.imwrite("Semaforo/3/"+str(cont_frames)+".jpg", imagem)	
			
			cont_frames += 1
			#print(status_a0, status_a1, status_a2, status_a3, status_b0, status_b1, status_b2, status_b3, status_visao_faixa_dir, status_visao_faixa_esq, status_obstaculo_vl53x)
			#print("A0:{:>5} A1:{:>5} A2:{:>5} A3:{:>5} \tB0:{:>5} B1:{:>5} B2:{:>5} B3:{:>5}".format(a0, a1, a2, a3, b0, b1, b2, b3))
			#print(DETECCAO_OBSTACULOS_VISAO)
			#print(status_visao_faixa_dir, status_visao_faixa_esq, status_normalidade_faixa_dir, status_normalidade_faixa_esq, DETECCAO_OBSTACULOS_VISAO)
			#print("\nDetectou Obstaculo: {0} \tValor: {1}".format(status_obstaculo_visao, 0))
			#print(status_placa_pare, status_placa_pedestre,	status_placa_desvio)
			#print(ft_dir_inf, ft_dir_sup, ft_esq_sup, ft_esq_inf)
			#print(ft_deteccao_faixa_dir_ext, ft_deteccao_faixa_dir_cen, ft_deteccao_faixa_esq_cen, ft_deteccao_faixa_esq_ext, status_visao_faixa_dir_ext, status_visao_faixa_esq_ext)


			capturaFrames.truncate(0)
			
			if cv2.waitKey(1) & 0xFF == 27:
				motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
				cv2.destroyAllWindows()
				GPIO.cleanup()
				break
	finally:
		print("bye bye...")	
		cv2.destroyAllWindows()
		GPIO.cleanup()
