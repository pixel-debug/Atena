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

cls_pare = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_pare_2.xml')

def detecta_placa(nome, img, classificador):
	

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array



	# Procurando caracteristicas semelhante na imagem capturada a partir do classificador
	detecta_obj = cls_pare.detectMultiScale(gray, 1.1, 5)

	for (x,y,w,h) in detecta_obj:
	    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
 
	# Apresenta imagem
	cv2.imshow("Frame", image)


	# limpa o buffer de quadros e prepara para receber o proximo
	rawCapture.truncate(0)

	if cv2.waitKey(1) & 0xFF == 27:
		break
	 
print("Cleaning up")
GPIO.cleanup()
