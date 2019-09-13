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
camera.resolution = (var.tam_original_tela_x, var.tam_original_tela_y)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(var.tam_original_tela_x, var.tam_original_tela_y))

def detecta_placas(img, nome, classificador):
	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	placa_detectada = classificador.detectMultiScale(img_gray, 1.1, 5)

	for (x,y,w,h) in placa_detectada:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

	for (x,y,w,h) in placa_detectada:
		cv2.putText(img, nome, (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
	
	for (x,y,w,h) in placa_detectada:
		distancia_placa = calculo_distancia_placa(x, w)

	return img

def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	imagem = frame.array

	reigao_placa = imagem[var.y1_img_placas_dir:var.y2_img_placas_dir, var.x1_img_placas_dir:var.x2_img_placas_dir]

	for (n, c) in var.classificadores:
		imagem_placas = detecta_placas(reigao_placa, n, c)
		#print(var.classificadores)
		#if a == "Pedestre":
		#	print("ok")
	#imagem_p2 = detecta_placas(var.nome_p2, reigao_placa, var.classificador_p2)

	#imagem_p3 = detecta_placas(var.nome_p3, reigao_placa, var.classificador_p3)



	# Apresenta imagem
	#cv2.imshow("Frame", imagem)

	cv2.imshow("Regiao Placa", reigao_placa)


	# limpa o buffer de quadros e prepara para receber o proximo
	rawCapture.truncate(0)

	if cv2.waitKey(1) & 0xFF == 27:
		break
	 
print("Cleaning up")
GPIO.cleanup()

