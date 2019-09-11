#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Placas

# --------------------------------------------------------

from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import cv2

# Inicializacao e configuracao da camera 
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array

	# Conversão da imagem para escala de cinza
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	# Procurando caracteristicas semelhante na imagem capturada a partir do classificador
	detecta_obj = classificador.detectMultiScale(gray, 1.1, )
