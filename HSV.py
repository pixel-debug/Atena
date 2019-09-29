#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: HSV

# --------------------------------------------------------

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# Inicializacao da camera e parâmetros de resolucao e quadros por segundo capturado
camera = PiCamera()
camera.resolution = (720, 560)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(720, 560))
time.sleep(0.1)


def placas_checkpoints(img, nome, min_H, max_H, min_S, max_S, min_V, max_V, area_min, area_max):
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	img_clone = img.copy()

	hsv_min = np.array([min_H, min_S, min_V])
	hsv_max = np.array([max_H, max_S, max_V])
	
	mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

	img_resultado = cv2.bitwise_and(img, img, mask=mascara)
	
	_, contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		if ((cv2.contourArea(c) > area_min) and (cv2.contourArea(c) < area_max)):
			x,y,w,h = cv2.boundingRect(c)
			distancia_placa = calculo_distancia_placa(x, w)
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 3)
			cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			cv2.putText(img, str(distancia_placa)+" cm", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			img_nova = img[y:(y+h),x:(x+w)]

			#print(x,y,w,h)
			return img_nova

def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)

def isola_placa1(img):
	return isola_placa(img,126,151,70,180,77,255,4000,50000)

def isola_placa2(img):
	return isola_placa(img,83,90,240,250,240,252,40000,50000)

def isola_placa3(img):
	return isola_placa(img,21,34,180,202,165,175,40000,50000)

def isola_placa_verde(img):
	return isola_placa(img,65,75,191,255,132,150,4000,50000)

def isola_placa_marrom(img):
	return isola_placa(img,7,15,122,231,135,180,4000,50000)


'''
def procura_placa(imagemCamera):
	if(imagemPlaca = isola_placa1(imagemCamera)):	
		stringPlaca = "museu"
	elif(imagemPlaca = isola_placa2(imagemCamera)):
		stringPlaca = "teatro"
	elif(imagemPlaca = isola_placa3(imagemCamera)):
		stringPlaca = "igreja"
	elif(imagemPlaca = isola_placa_verde(imagemCamera)):	
		stringPlaca = 'verde'
	elif(imagemPlaca = isola_placa_marrom(imagemCamera)):	
		stringPlaca = "marrom"
	else:
		stringPlaca = "nada"
	
	cv2.imshow(stringPlaca,imagemPlaca)
	return stringPlaca
'''


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array
	

	nome_check_1 = "Museu."
	placa_check_1 = placas_checkpoints(imagem, nome_check_1,126,151,70,180,77,255,4000,50000)
	

	'''
	placa_check_2 = isola_placa(imagem,126,151,70,180,77,255,4000,50000)	
	nome_check_2 = "Igreja."	

	placa_check_3 = isola_placa(imagem,126,151,70,180,77,255,4000,50000)
	nome_check_3 = "Teatro."
	'''

	#cv2.imshow("dsdfas",stringPlaca)

	# Apresenta as imagens capturas por meio dos frames
	cv2.imshow("Streaming Camera Atena", imagem)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'q' sai do programa
	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()
