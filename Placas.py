#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Placas

# --------------------------------------------------------
import cv2
import Variaveis as var

def detecta_placa(img, classificadores):
	deteccao, nome_real, distancia_placa = " - ",  " - ", " - "
	val_pare, val_pedestre, val_desvio =  False, False, False

	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	for c in classificadores:
		nome, classificador = c
		
		img_detecta_placa = classificador.detectMultiScale(img_gray, 1.2, 10)
		
		for (x,y,w,h) in img_detecta_placa:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		for (x,y,w,h) in img_detecta_placa:
			distancia_placa = calculo_distancia_placa(x, w)

		for (x,y,w,h) in img_detecta_placa:
			cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			cv2.putText(img, str(distancia_placa)+" cm", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			if nome == var.nome_p1:
				nome_real = nome
				val_pare = True
				deteccao = val_pare
			if nome == var.nome_p2:
				nome_real = nome
				val_pedestre = True
				deteccao = val_pedestre
			if nome == var.nome_p3:
				nome_real = nome
				val_desvio = True
				deteccao = val_desvio 

		
	return deteccao, nome_real, distancia_placa

def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)


'''
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



for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	imagem = frame.array

	reigao_placa = imagem[var.y1_img_placas_dir:var.y2_img_placas_dir, var.x1_img_placas_dir:var.x2_img_placas_dir]

	detectou_placa, nome_placa, distancia_placa = detecta_placas(imagem, var.classificadores)
	
	print("Detectou Placa: {0} \tNome Placa: {1} \tDistancia Placa: {2}".format(detectou_placa, nome_placa, distancia_placa))
	
	# Apresenta imagem
	cv2.imshow("Frame", imagem)

	cv2.imshow("Regiao Placa", reigao_placa)


	# limpa o buffer de quadros e prepara para receber o proximo
	rawCapture.truncate(0)

	if cv2.waitKey(1) & 0xFF == 27:
		break
	 
print("Cleaning up")
GPIO.cleanup()
'''


