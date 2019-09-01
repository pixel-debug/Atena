#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste Classificadores

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

classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/haarcascade_frontalface_default.xml')

# Captura dos quadros por segundo
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array



print("Cleaning up")
GPIO.cleanup()

