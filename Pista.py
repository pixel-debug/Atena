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


pt_pista_1, pt_pista_2, pt_pista_3, pt_pista_4 = (60,580), (740,580), (15,645), (785,645)

pontos_pista = np.float32([[pt_pista_1], [pt_pista_2], [pt_pista_3], [pt_pista_4]])

def perspectiva_pista(imagem):
	cv2.line(imagem, pt_pista_1, pt_pista_2, (0,0,255), 4)
	cv2.line(imagem, pt_pista_1, pt_pista_3, (0,0,255), 4)
	cv2.line(imagem, pt_pista_2, pt_pista_4, (0,0,255), 4)
	cv2.line(imagem, pt_pista_3, pt_pista_4, (0,0,255), 4)

	return imagem
	


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array

	imagem = perspectiva_pista(imagem)

	tela.apresenta_imagem("Imagem Original", imagem, 30, 30)
	#cv2.imshow("Streaming Camera Atena", imagem)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'q' sai do programa
	if cv2.waitKey(1) & 0xFF == 27:
		break
	
	

cv2.destroyAllWindows()

