#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Main

# --------------------------------------------------------
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import RPi.GPIO as GPIO
import Configuracoes as definir
import Motores as motor
import Sensores as sensor
import Tratamento as trata
import Variaveis as var
import Tela as tela
import Interface as interface
#import HSV as hsv
import time


frames = PiCamera()
frames.resolution = (var.tam_original_tela_x, var.tam_original_tela_y)
frames.framerate = var.taxa_quadros
capturaFrames = PiRGBArray(frames, size=(var.tam_original_tela_x, var.tam_original_tela_y))

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

ctr_vel_motor_dir = GPIO.PWM(var.pin_ENA, 500)
ctr_vel_motor_dir.start(0)

ctr_vel_motor_esq = GPIO.PWM(var.pin_ENB, 500)
ctr_vel_motor_esq.start(0)


time.sleep(1)

inicia = False
inicializacao = False
'''
while(inicia is False):
	opcao_destino = interface.menu_texto()	
	inicializacao, ck1, ck2, ck3 = trata.interface_menu(opcao_destino)
	inicia = inicializacao
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
			ft_dir_inf, ft_dir_sup, ft_esq_sup, ft_esq_inf = sensor.fototransistores()

			# Obtendo valores brutos sensor de obstaculo 
			#distancia_obstaculo = sensor.vl530x()	
			# -------------------------------------------------------------------

					
			# -------------- Obtentendo Respostas dos Tratamentos ---------------
			# Deteccao das faixas na pista
			(
				imagem_perspectiva_pista,
				imagem_faixa_esq, 
	   			imagem_faixa_dir,
				deteccao_fototransistor_dir_inf,
				deteccao_fototransistor_dir_sup, 
				deteccao_fototransistor_esq_sup, 
				deteccao_fototransistor_esq_inf, 
				vs_deteccao_faixa_dir, 
				vs_deteccao_faixa_esq,
				status_normalidade_faixa_dir, 
				status_normalidade_faixa_esq
			) = trata.deteccao_faixas_pista(imagem_pista, ft_dir_inf, ft_dir_sup, ft_esq_sup, ft_esq_inf)


			# Deteccao de obstaculos na pista
			(
				imagem_obstaculos,
				status_obstaculo_visao, 
				status_obstaculo_vl53x, 
			) = trata.deteccao_obstaculo(imagem_obstaculo, 0)					
			#deteccao_obstaculo = False


			# Deteccao de placas na pista
			(
				imagem_detecao_placa,
				deteccao_placa_pare, 
				deteccao_placa_pedestre, 
				deteccao_placa_desvio 
			) = trata.deteccao_placas(imagem)
			# -------------------------------------------------------------------
			

			# ------------------- Apresentacao Telas ----------------------------
			#tela.apresenta("Imagem Original", imagem, 10, 10)
			tela.apresenta("Imagem obstaculos", imagem_obstaculos, 10, 10)
			#tela.apresenta("Imagem Placas", imagem_detecao_placa, 500, 10)
			tela.apresenta("Imagem Perspe", imagem_perspectiva_pista, 500, 10)
			tela.apresenta("Imagem Faixa Esquerda", imagem_faixa_esq, 10, 400)
			tela.apresenta("Imagem Faixa Direita", imagem_faixa_dir, 500, 400)
			# -------------------------------------------------------------------


			# ------------------ DEFININDO CHAVES ESPECIAIS ---------------------
			MOVIMENTO_FRENTE_LIBERADO = False
			DETECCAO_FAIXA_DIR_FOTO = False
			DETECCAO_FAIXA_ESQ_FOTO = False 
			DETECCAO_FAIXA_DIR_VISAO = False
			DETECCAO_FAIXA_ESQ_VISAO = False

			# Condicao para o robo ter movimento liberado
			if(
			  (deteccao_fototransistor_dir_inf is False) and 
			  (deteccao_fototransistor_dir_sup is False) and 
			  (deteccao_fototransistor_esq_inf is False) and 
			  (deteccao_fototransistor_esq_sup is False) and 
			  (vs_deteccao_faixa_dir is False) and 
			  (vs_deteccao_faixa_esq is False) and
			  (deteccao_obstaculo is False)	
			 ):
				MOVIMENTO_FRENTE_LIBERADO = True	

			# Condicao para o robo fazer a correcao para a esquerda a partir dos fototransistores
			if(
			  (deteccao_fototransistor_dir_inf is True) or 
			  (deteccao_fototransistor_dir_sup is True)
			 ):
				DETECCAO_FAIXA_DIR_FOTO = True

			# Condicao para o robo fazer a correcao para a direita a partir dos fototransistores
			if(
			  (deteccao_fototransistor_esq_inf is True) or 
			  (deteccao_fototransistor_esq_sup is True)
			 ):
				DETECCAO_FAIXA_ESQ_FOTO = True

			# Condicao para o robo fazer a correcao para a direita a partir da visao
			if(vs_deteccao_faixa_dir is True):
				DETECCAO_FAIXA_DIR_VISAO = True

			# Condicao para o robo fazer a correcao para a esquerda a partir da visao
			if(vs_deteccao_faixa_esq is True):
				DETECCAO_FAIXA_ESQ_VISAO = True
			# -------------------------------------------------------------------
			
			
			# ----------------- Condicionais De Movimentacao --------------------
			# Seguir em frente			
			if(MOVIMENTO_FRENTE_LIBERADO is True):
				#print("Seguir frente")				
				motor.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq) 
			
			# Detccao faixa direita
			elif (DETECCAO_FAIXA_DIR_FOTO is True):
				vs_deteccao_faixa_dir = False
				deteccao_fototransistor_dir_inf = True
				while(deteccao_fototransistor_dir_inf is not False):
					#print("Virar Esquerda") 
					motor.movimento_esquerda(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					deteccao_fototransistor_dir_inf = False

			# Detccao faixa esquerda
			elif (DETECCAO_FAIXA_ESQ_FOTO is True):
				vs_deteccao_faixa_esq = False
				deteccao_fototransistor_esq_inf = True
				while(deteccao_fototransistor_esq_inf is not False):
					#print("Virar Direita") 
					motor.movimento_esquerda(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					deteccao_fototransistor_esq_inf = False
			
	
			# Detccao faixa direita visao computacional
			elif (DETECCAO_FAIXA_DIR_VISAO is True):
				if((deteccao_fototransistor_dir_inf is False) and (deteccao_fototransistor_dir_sup is False)):
					while(DETECCAO_FAIXA_DIR_VISAO is not False):
						#print("Virar Esquerda com Visao") 
						motor.movimento_esquerda(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
						DETECCAO_FAIXA_DIR_VISAO = False						
			

			# Detccao faixa esquerda visao computacional
			elif (DETECCAO_FAIXA_ESQ_VISAO is True):
				if((deteccao_fototransistor_esq_inf is  False) and (deteccao_fototransistor_esq_sup is  False)):
					while(DETECCAO_FAIXA_ESQ_VISAO is not False):
						#print("Virar Direita com Visao") 
						motor.movimento_direita(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
						DETECCAO_FAIXA_ESQ_VISAO = False
		

			# Qualquer anomalia, manter robô parado!
			else:
				print("Parando")	
				motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
			# -------------------------------------------------------------------



			# -------------------- Condicionais Placas---------------------------
			if(deteccao_placa_pare is True):
				trata.placa_pare(ctr_vel_motor_dir, ctr_vel_motor_esq)
			elif(deteccao_placa_pedestre is True):
				trata.placa_pedestre(ctr_vel_motor_dir, ctr_vel_motor_esq)
								
					
			# -------------------------------------------------------------------	

			
				
			
			cont_frames += 1
			#print(cont_frames)
			#print(deteccao_placa_pare, deteccao_placa_pedestre,	deteccao_placa_desvio)
			#print(ft_dir_inf, ft_dir_sup, ft_esq_sup, ft_esq_inf)
			#print(ft_deteccao_faixa_dir_ext, ft_deteccao_faixa_dir_cen, ft_deteccao_faixa_esq_cen, ft_deteccao_faixa_esq_ext, vs_deteccao_faixa_dir_ext, vs_deteccao_faixa_esq_ext)


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
