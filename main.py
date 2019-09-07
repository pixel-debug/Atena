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
import Variaveis as var
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

controle_velocidade_direita = GPIO.PWM(var.pin_ENA, 500)
controle_velocidade_direita.start(0)

controle_velocidade_esquerda = GPIO.PWM(var.pin_ENB, 500)
controle_velocidade_esquerda.start(0)

frames = PiCamera()
frames.resolution = (var.tam_tela_x, var.tam_tela_y)
frames.framerate = var.taxa_quadros
capturaFrames = PiRGBArray(frames, size=(var.tam_tela_x, var.tam_tela_y))

print("Inicializando Sistema...")
time.sleep(0.5)
print("Pronto!")

class main:
	try:
		for frame in frames.capture_continuous(capturaFrames, format="bgr", use_video_port=True):
			imagem = frame.array
			
			# Obtendo valores brutos dos sensores
			ft_dir_extrem, ft_dir_centro, ft_esq_centro, ft_esq_extrem = sensor.fototransistor()
			distancia_obstaculo = sensor.obstaculo()			
			print(ft_dir_extrem, ft_dir_centro, ft_esq_centro, ft_esq_extrem, distancia_obstaculo)
			

			cv2.imshow("Imagem Original", imagem)
			capturaFrames.truncate(0)
			if cv2.waitKey(1) & 0xFF == 27:
				break
	finally:
		print("Cleaning up")
		cv2.destroyAllWindows()
		GPIO.cleanup()
