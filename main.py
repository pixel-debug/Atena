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
import time


frames = PiCamera()
frames.resolution = (var.tam_original_tela_x, var.tam_original_tela_y)
frames.framerate = var.taxa_quadros
capturaFrames = PiRGBArray(frames, size=(var.tam_original_tela_x, var.tam_original_tela_y))

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

controle_velocidade_direita = GPIO.PWM(var.pin_ENA, 500)
controle_velocidade_direita.start(0)

controle_velocidade_esquerda = GPIO.PWM(var.pin_ENB, 500)
controle_velocidade_esquerda.start(0)


time.sleep(1)

global opcao_destino

opcao_destino = interface.menu_texto()	
ck1, ck2, ck3 = trata.interface_menu(opcao_destino)

class main:
	try:
		for frame in frames.capture_continuous(capturaFrames, format="bgr", use_video_port=True):
					
			print(ck1, ck2, ck3)	
			
			# ------------------- Obtencao valores sensores ----------------------
			# Obtendo quadros capturados pela camera
			imagem = frame.array

			# Obtendo valores brutos dos fototransistores
			ft_dir_inf, ft_dir_sup, ft_esq_sup, ft_esq_inf = sensor.fototransistores()

			# Obtendo valores brutos sensor de obstaculo 
			#distancia_obstaculo = sensor.vl530x()	
			# -------------------------------------------------------------------

		
			# -------------- Obtentendo Respostas dos Tratamentos ---------------
			# Deteccao das faixas na pista
			(
				deteccao_fototransistor_dir_inf,
				deteccao_fototransistor_dir_sup, 
				deteccao_fototransistor_esq_sup, 
				deteccao_fototransistor_esq_inf, 
				vs_deteccao_faixa_dir, 
				vs_deteccao_faixa_esq
			) = trata.deteccao_faixas_pista(imagem, ft_dir_inf, ft_dir_sup, ft_esq_sup, ft_esq_inf)

			# Deteccao de obstaculos na pista
			#deteccao_obstaculo = trata.deteccao_obstaculo(distancia_obstaculo)
			deteccao_obstaculo = False			

			# Deteccao de placas na pista
			(
				deteccao_placa_pare, 
				deteccao_placa_pedestre, 
				deteccao_placa_desvio 
			) = trata.deteccao_placas(imagem)
			# -------------------------------------------------------------------

			#print(deteccao_placa_pare, deteccao_placa_pedestre, deteccao_placa_desvio)
			
						
			# ------------------- Condicionais principais -------------------------
			# Seguir em frente			
			if(
			  (deteccao_fototransistor_dir_inf is False) and 
			  (deteccao_fototransistor_dir_sup is False) and 
			  (deteccao_fototransistor_esq_inf is False) and 
			  (deteccao_fototransistor_esq_sup is False) and 
			  (vs_deteccao_faixa_dir is False) and 
			  (vs_deteccao_faixa_esq is False) and
			  (deteccao_obstaculo is False)
			  ):
				#print("Seguir frente")				
				motor.movimento_frente(controle_velocidade_direita, controle_velocidade_esquerda) 
			

			# Detccao faixa direita
			elif ((deteccao_fototransistor_dir_inf is True) or (deteccao_fototransistor_dir_sup is True)):
				vs_deteccao_faixa_dir = False
				deteccao_fototransistor_dir_inf = True
				while(deteccao_fototransistor_dir_inf is not False):
					#print("Virar Esquerda") 
					motor.movimento_esquerda(var.velocidade, controle_velocidade_direita, controle_velocidade_esquerda)
					deteccao_fototransistor_dir_inf = False


			# Detccao faixa esquerda
			elif ((deteccao_fototransistor_esq_inf is True) or (deteccao_fototransistor_esq_sup is True)):
				vs_deteccao_faixa_esq = False
				deteccao_fototransistor_esq_inf = True
				while(deteccao_fototransistor_esq_inf is not False):
					#print("Virar Direita") 
					motor.movimento_esquerda(var.velocidade, controle_velocidade_direita, controle_velocidade_esquerda)
					deteccao_fototransistor_esq_inf = False
			
	
			# Detccao faixa direita visao computacional
			elif (vs_deteccao_faixa_dir is True):
				if((deteccao_fototransistor_dir_inf is False) and (deteccao_fototransistor_dir_sup is False)):
					while(vs_deteccao_faixa_dir is not False):
						#print("Virar Esquerda com Visao") 
						motor.movimento_esquerda(var.velocidade, controle_velocidade_direita, controle_velocidade_esquerda)
						vs_deteccao_faixa_dir = False						
			

			# Detccao faixa esquerda visao computacional
			elif (vs_deteccao_faixa_esq is True):
				if((deteccao_fototransistor_esq_inf is  False) and (deteccao_fototransistor_esq_sup is  False)):
					while(vs_deteccao_faixa_esq is not False):
						#print("Virar Direita com Visao") 
						motor.movimento_direita(var.velocidade, controle_velocidade_direita, controle_velocidade_esquerda)
						vs_deteccao_faixa_esq = False
		

			# Qualquer anomalia, manter robô parado!
			else:
				print("Parando")	
				motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
			# -------------------------------------------------------------------


			if(deteccao_placa_pare is True):
				trata.placa_pare(controle_velocidade_direita, controle_velocidade_esquerda)
			if(deteccao_placa_pedestre is True):
				print("placa pedestre...")
				trata.placa_pare(controle_velocidade_direita, controle_velocidade_esquerda)
				#trata.placa_pedestre(controle_velocidade_direita, controle_velocidade_esquerda, deteccao_fototransistor_dir_sup, deteccao_fototransistor_esq_sup)

			
				
			
			

			#print(ft_dir_inf, ft_dir_sup, ft_esq_sup, ft_esq_inf)
			#print(ft_deteccao_faixa_dir_ext, ft_deteccao_faixa_dir_cen, ft_deteccao_faixa_esq_cen, ft_deteccao_faixa_esq_ext, vs_deteccao_faixa_dir_ext, vs_deteccao_faixa_esq_ext)


			capturaFrames.truncate(0)
			
			if cv2.waitKey(1) & 0xFF == 27:
				motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
				cv2.destroyAllWindows()
				GPIO.cleanup()
				break
	finally:
		print("bye bye...")	
		cv2.destroyAllWindows()
		GPIO.cleanup()
