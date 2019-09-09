#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Pista

# --------------------------------------------------------

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import Tela as tela
import Variaveis as var


# Inicializacao da camera e parâmetros de resolucao e quadros por segundo capturado
camera = PiCamera()
camera.resolution = (var.tam_original_tela_x, var.tam_original_tela_y)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(var.tam_original_tela_x, var.tam_original_tela_y))
time.sleep(0.1)


pt_pista_1, pt_pista_2, pt_pista_3, pt_pista_4 = (50,570), (750,570), (5,635), (795,635)
pt_destino_1, pt_destino_2, pt_destino_3, pt_destino_4 = (160,0), (640,0), (160,680), (640,680)


pontos_pista = np.float32([[pt_pista_1], [pt_pista_2], [pt_pista_3], [pt_pista_4]])
pontos_destino = np.float32([[pt_destino_1], [pt_destino_2], [pt_destino_3], [pt_destino_4]])


def perspectiva_pista(img):
	cv2.line(img, pt_pista_1, pt_pista_2, (0,0,255), 4)
	cv2.line(img, pt_pista_1, pt_pista_3, (0,0,255), 4)
	cv2.line(img, pt_pista_2, pt_pista_4, (0,0,255), 4)
	cv2.line(img, pt_pista_3, pt_pista_4, (0,0,255), 4)

	cv2.line(img, pt_destino_1, pt_destino_2, (0,255,0), 4)
	cv2.line(img, pt_destino_1, pt_destino_3, (0,255,0), 4)
	cv2.line(img, pt_destino_2, pt_destino_4, (0,255,0), 4)
	cv2.line(img, pt_destino_3, pt_destino_4, (0,255,0), 4)

	matriz = cv2.getPerspectiveTransform(pontos_pista, pontos_destino)
	img = cv2.warpPerspective(imagem, matriz, (var.tam_original_tela_x, var.tam_original_tela_y)) 
	return img
	

def detecta_faixas(img):


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array

	imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
	
	imagem_perpectiva_pista = perspectiva_pista(imagem)

	tela.apresenta("Imagem Original", imagem, 10, 30)
	tela.apresenta("Perspectiva Pista", imagem_perpectiva_pista, 10, 375)
	
	#cv2.imshow("Streaming Camera Atena", imagem)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'q' sai do programa
	if cv2.waitKey(1) & 0xFF == 27:
		break
	
	

cv2.destroyAllWindows()

