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

print("Inicializando Sistema...")
time.sleep(0.5)
print("Pronto!")

contador_tempo = 0

class main:
	try:
		for frame in frames.capture_continuous(capturaFrames, format="bgr", use_video_port=True):	
			
			# ------------------- Obtencao valores sensores ----------------------
			# Obtendo quadros capturados pela camera
			imagem = frame.array

			# Obtendo valores brutos dos fototransistores
			ft_dir_ext, ft_dir_cen, ft_esq_cen, ft_esq_ext = sensor.fototransistores()

			# Obtendo valores brutos sensor de obstaculo 
			distancia_obstaculo = sensor.vl530x()	
			# -------------------------------------------------------------------

		
			# -------------- Obtentendo Respostas dos Tratamentos ---------------
			# Deteccao das faixas na pista
			(
				ft_deteccao_faixa_dir_ext,
				ft_deteccao_faixa_dir_cen, 
				ft_deteccao_faixa_esq_cen, 
				ft_deteccao_faixa_esq_ext, 
				vs_deteccao_faixa_dir_ext, 
				vs_deteccao_faixa_esq_ext
			) = trata.deteccao_faixas_pista(imagem, ft_dir_ext, ft_dir_cen, ft_esq_cen, ft_esq_ext)

			# Deteccao de obstaculos na pista
			deteccao_obstaculo = trata.deteccao_obstaculo(distancia_obstaculo)
					

			# Deteccao de placas na pista
			(
				deteccao_placa_pare, 
				deteccao_placa_pedestre, 
				deteccao_placa_desvio 
			) = trata.deteccao_placas(imagem)
			# -------------------------------------------------------------------

			#print(deteccao_placa_pare, deteccao_placa_pedestre, deteccao_placa_desvio)
			
			motor.movimento_frente(controle_velocidade_direita, controle_velocidade_esquerda)
			print("Frente")			
			if(deteccao_placa_pare is True):
				#contador_tempo = 0
				print("placa detectada! Aguardando...")
				motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
				time.sleep(4)
				motor.movimento_frente(controle_velocidade_direita, controle_velocidade_esquerda)
				time.sleep(2)
				deteccao_placa_pare = False
				'''
				while(contador_tempo <= 200):
					motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)	
					print(contador_tempo)					
					contador_tempo += 1
				'''			

			

			

			'''				
			# ------------------- Condicionais principais -------------------------
			# Seguir em frente			
			if(
			(ft_deteccao_faixa_dir_ext is False) and 
			(ft_deteccao_faixa_dir_cen is False) and 
			(ft_deteccao_faixa_esq_cen is False) and 
			(ft_deteccao_faixa_esq_ext is False) and  
			(vs_deteccao_faixa_dir_ext is False) and 
			(vs_deteccao_faixa_esq_ext is False) and
			(deteccao_obstaculo is False)
			):
				#print("Seguir frente")				
				motor.movimento_frente(controle_velocidade_direita, controle_velocidade_esquerda) 

			# Detccao faixa direita
			elif (((ft_deteccao_faixa_dir_ext is  True) or (ft_deteccao_faixa_dir_cen is  True))):
				vs_deteccao_faixa_dir_ext = False
				while(ft_deteccao_faixa_dir_ext is not False):
					#print("Virar Esquerda") 
					motor.movimento_esquerda(controle_velocidade_direita, controle_velocidade_esquerda)
					ft_deteccao_faixa_dir_ext = False

			# Detccao faixa direita
			elif (((ft_deteccao_faixa_esq_ext is  True) or (ft_deteccao_faixa_esq_cen is  True))):
				vs_deteccao_faixa_esq_ext = False
				while(ft_deteccao_faixa_dir_ext is not False):
					#print("Virar Direira") 
					motor.movimento_direita(controle_velocidade_direita, controle_velocidade_esquerda)
					ft_deteccao_faixa_esq_ext = False

			elif (vs_deteccao_faixa_dir_ext is True):
				if((ft_deteccao_faixa_dir_ext is False) and (ft_deteccao_faixa_dir_cen is False)):
					while(vs_deteccao_faixa_dir_ext is not False):
						print("Virar Esquerda") 
						motor.movimento_esquerda(controle_velocidade_direita, controle_velocidade_esquerda)
						vs_deteccao_faixa_dir_ext = False						

			elif (vs_deteccao_faixa_esq_ext is True):
				if((ft_deteccao_faixa_esq_ext is  False) and (ft_deteccao_faixa_esq_cen is  False)):
					while(vs_deteccao_faixa_esq_ext is not False):
						print("Virar Direita") 
						motor.movimento_direita(controle_velocidade_direita, controle_velocidade_esquerda)
						vs_deteccao_faixa_esq_ext = False

			# Qualquer anomalia, manter robô parado!
			else:
				print("Parando")	
				motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
			# -------------------------------------------------------------------
			'''
			
			


			
			'''
			# Somente fototransistores
			# ------------------- Condicionais principal -------------------------
			# Seguir em frente			
			if((deteccao_faixa_dir_ext is False) and (deteccao_faixa_dir_cen is False) and (deteccao_faixa_esq_cen is False) and (deteccao_faixa_esq_ext is False) and (deteccao_obstaculo is False)):
				#print("Seguir frente")				
				motor.movimento_frente(controle_velocidade_direita, controle_velocidade_esquerda) 

			# Detccao faixa direita
			elif (((deteccao_faixa_dir_ext is  True) or (deteccao_faixa_dir_cen is  True))):
					while(deteccao_faixa_dir_ext is not False):
						#print("Virar Esquerda") 
						motor.movimento_esquerda(controle_velocidade_direita, controle_velocidade_esquerda)
						deteccao_faixa_dir_ext = False
			
			# Detccao faixa esquerda
			elif (((deteccao_faixa_esq_ext is  True) or (deteccao_faixa_esq_cen is  True))):
					while(deteccao_faixa_esq_ext is not False):
						#print("Virar Direita") 
						motor.movimento_direita(controle_velocidade_direita, controle_velocidade_esquerda)
						deteccao_faixa_esq_ext = False
			
			# Qualquer anomalia, manter robô parado!
			else:
				#print("Parando")
				motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
			# -------------------------------------------------------------------
			'''

			#print(ft_dir_ext, ft_dir_cen, ft_esq_cen, ft_esq_ext)
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
