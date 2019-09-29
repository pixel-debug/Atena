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
	autorizado, ck1, ck2, ck3 = trata.interface_menu(opcao_destino)
	inicializacao = autorizado
'''



# 138 frames em 1 minuto
cont_frames = 0

class main:
	try:
		for frame in frames.capture_continuous(capturaFrames, format="bgr", use_video_port=True):
			
			# ------------------- Obtencao valores sensores ----------------------
			# Obtendo quadros capturados pela camera
			imagem = frame.array

			imagem_pista = imagem.copy()
			imagem_obstaculo = imagem.copy()
			
			# Obtendo valores brutos dos fototransistores
			a0, a1, a2, a3, b0, b1, b2, b3 = sensor.fototransistores()

			# Obtendo valores brutos sensor de obstaculo 
			#distancia_obstaculo = sensor.vl530x()	
			# -------------------------------------------------------------------

					
			# -------------- Obtentendo Respostas dos Tratamentos ---------------
			# Deteccao das faixas na pista
			(
				imagem_perspectiva_pista,
				imagem_faixa_esq, 
	   			imagem_faixa_dir,
				status_a0, 
				status_a1, 
				status_a2, 
				status_a3,
				status_b0, 
				status_b1, 
				status_b2, 
				status_b3,
				status_visao_faixa_dir, 
				status_visao_faixa_esq,
				status_anormalidade_faixa_dir, 
				status_anormalidade_faixa_esq
			) = trata.deteccao_faixas_pista(imagem_pista, a0, a1, a2, a3, b0, b1, b2, b3)


			# Deteccao de obstaculos na pista
			(
				imagem_obstaculos,
				status_obstaculo_visao, 
				status_obstaculo_vl53x, 
			) = trata.deteccao_obstaculo(imagem_obstaculo, 0)					
			

			# Deteccao de placas na pista
			(
				imagem_detecao_placa,
				status_placa_pare, 
				status_placa_pedestre, 
				status_placa_desvio 
			) = trata.deteccao_placas(imagem)
			# -------------------------------------------------------------------
			

			# ------------------ DEFININDO CHAVES ESPECIAIS ---------------------
			MOVIMENTO_FRENTE_LIBERADO = False

			DETECCAO_FAIXA_DIR_VISAO = False
			DETECCAO_FAIXA_ESQ_VISAO = False

			DETECCAO_OBSTACULOS_VISAO = False

			# Condicao para o robo ter movimento liberado
			if(
			  (status_a0 is False) and 
			  (status_a1 is False) and 
			  (status_a2 is False) and 
			  (status_a3 is False) and
			  (status_b0 is False) and 
			  (status_b1 is False) and 
			  (status_b2 is False) and 
			  (status_b3 is False) and  
			  (status_visao_faixa_dir is False) and 
			  (status_visao_faixa_esq is False) and
			  (status_obstaculo_vl53x is False)
			  ):
				MOVIMENTO_FRENTE_LIBERADO = True	

			# Condicao para o robo fazer a correcao para a direita a partir da visao
			if(status_visao_faixa_dir is True):
				DETECCAO_FAIXA_DIR_VISAO = True

			# Condicao para o robo fazer a correcao para a esquerda a partir da visao
			if(status_visao_faixa_esq is True):
				DETECCAO_FAIXA_ESQ_VISAO = True

			'''
			# Condicao para o robo fazer a verificacao de obstaculos a partir da visao
			if(
			  (status_visao_faixa_dir is False) and 
			  (status_visao_faixa_esq is False) and
			  (status_anormalidade_faixa_dir is False) and
			  (status_anormalidade_faixa_esq is False)
			  ):
				DETECCAO_OBSTACULOS_VISAO = status_obstaculo_visao
			else:
				DETECCAO_OBSTACULOS_VISAO = False
			'''			
			# -------------------------------------------------------------------
			
			
			# ------------------ *** Condicionais De Movimentacao *** ------------------------
			
			# ------------------ Seguir em frente ou manter robô parado ----------------------	
			if(MOVIMENTO_FRENTE_LIBERADO is True):
				print("Seguindo em frente...")
				gerencia.seguir_em_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)			
			else:
				print("Anomalia, manter robô parado!")	
				motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
			# --------------------------------------------------------------------------------


			# -------------------- Detccao faixa direita Visao Comp --------------------------
			if (DETECCAO_FAIXA_DIR_VISAO is True):	
				while(DETECCAO_FAIXA_DIR_VISAO is not False):
					print("Virar Esquerda com Visao") 
					motor.movimento_esquerda(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					DETECCAO_FAIXA_DIR_VISAO = False						
			# --------------------------------------------------------------------------------
	

			# -------------------- Detccao faixa esquerda Visao Comp -------------------------
			if (DETECCAO_FAIXA_ESQ_VISAO is True):
				while(DETECCAO_FAIXA_ESQ_VISAO is not False):
					print("Virar Direita com Visao") 
					motor.movimento_direita(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					DETECCAO_FAIXA_ESQ_VISAO = False
			# --------------------------------------------------------------------------------
			

			# -------------------------- Detccao faixa direita -------------------------------
			if (status_a0 is True):
				while(status_a0 is not False):
					print("Virar Esquerda A0")
					a0, _, _, _, _, _, _, _ = sensor.fototransistores() 
					motor.movimento_direita(var.velReacao, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(a0 >= var.CONST_A0): 
						status_a0 = False

			if (status_a1 is True):
				while(status_a1 is not False):
					print("Virar Esquerda A1")
					_, a1, _, _, _, _, _, _ = sensor.fototransistores() 
					motor.movimento_direita(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(a1 >= var.CONST_A1): 
						status_a1 = False

			if (status_a2 is True):
				while(status_a2 is not False):
					print("Virar Esquerda A2")
					_, _, a2, _, _, _, _, _ = sensor.fototransistores() 
					motor.movimento_direita(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(a2 >= var.CONST_A2): 
						status_a2 = False
			# --------------------------------------------------------------------------------	

			# ------------------------- Detccao faixa esquerda -------------------------------
			if (status_b0 is True):
				while(status_b0 is not False):
					print("Virar Direita B0")
					_, _, _, _, b0, _, _, _ = sensor.fototransistores() 
					motor.movimento_esquerda(var.velReacao, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(b0 >= var.CONST_B0): 
						status_b0 = False

			if (status_b1 is True):
				while(status_b1 is not False):
					print("Virar Direita B1")
					_, _, _, _, _, b1, _, _ = sensor.fototransistores() 
					motor.movimento_esquerda(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(b1 >= var.CONST_B1): 
						status_b1 = False

			if (status_b2 is True):
				while(status_b2 is not False):
					print("Virar Direita B2")
					_, _, _, _, _, _, b2, _ = sensor.fototransistores() 
					motor.movimento_esquerda(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(b2 >= var.CONST_B2): 
						status_b2 = False
			# -------------------------------------------------------------------------------



			



			# -------------------- Condicionais Placas---------------------------
			if(status_placa_pare is True):
				gerencia.placa_pare(ctr_vel_motor_dir, ctr_vel_motor_esq)
			elif(status_placa_pedestre is True):
				gerencia.placa_pedestre(ctr_vel_motor_dir, ctr_vel_motor_esq)
			elif(status_placa_desvio is True):
				gerencia.placa_desvio(ctr_vel_motor_dir, ctr_vel_motor_esq)
								
					
			# -------------------------------------------------------------------	

			

			# ------------------- Apresentacao Telas ----------------------------
			tela.apresenta("Imagem Original", imagem, 10, 10)

			tela.apresenta("Imagem Placas", imagem_detecao_placa, 1000, 10)
			tela.apresenta("Imagem obstaculos", imagem_obstaculos, 500, 10)
			#tela.apresenta("Imagem Perspe", imagem_perspectiva_pista, 500, 10)
			tela.apresenta("Imagem Faixa Esquerda", imagem_faixa_esq, 10, 400)
			tela.apresenta("Imagem Faixa Direita", imagem_faixa_dir, 500, 400)
			# -------------------------------------------------------------------
				
			
			cont_frames += 1
			print("A0:{:>5} A1:{:>5} A2:{:>5} A3:{:>5} \tB0:{:>5} B1:{:>5} B2:{:>5} B3:{:>5}".format(a0, a1, a2, a3, b0, b1, b2, b3))
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
