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
import Variaveis as var

# Inicializacao e configuracao da camera 
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

def detecta_placa(nome, img, classificador):
	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	placa_detectada = classificador.detectMultiScale(img_gray, 1.1, 5)

	for (x,y,w,h) in placa_detectada:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	
	for (x,y,w,h) in placa_detectada:
		print(calculo_distancia_placa(x, w))

	return img

def calculo_distancia_placa(x, w):
	return ((x+w)-x)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array

	image = detecta_placa("Pare", image, var.classificador_pare)
 
	# Apresenta imagem
	cv2.imshow("Frame", image)


	# limpa o buffer de quadros e prepara para receber o proximo
	rawCapture.truncate(0)

	if cv2.waitKey(1) & 0xFF == 27:
		break
	 
print("Cleaning up")
GPIO.cleanup()

