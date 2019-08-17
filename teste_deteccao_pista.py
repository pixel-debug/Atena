#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste Detecção Pista

# --------------------------------------------------------

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


# Inicializacao da camera, definicao dos parametros de resolucao e dos quadros capturados por segundo capturado
camera = PiCamera()
camera.resolution = (360, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(360, 240))
time.sleep(0.1)

ponto1, ponto2, ponto3, ponto4 = (48,208), (255,208), (29,235), (276,235), 
pontos = [ponto1, ponto2, ponto3, ponto4]

# Funcao para regiao de interesse
def regiao_de_interesse():
	cv2.line(imagem, ponto1, ponto2, (0,0,255), 2)
	cv2.line(imagem, ponto1, ponto3, (0,0,255), 2)
	cv2.line(imagem, ponto2, ponto4, (0,0,255), 2)
	cv2.line(imagem, ponto3, ponto4, (0,0,255), 2)
	

# Funcao para rotacionar a imagem 180 graus
def rotaciona_imagem(imagem):
	(altura, largura) = imagem.shape[:2]
	centro_imagem = (largura / 2, altura / 2)
	matriz_imagem = cv2.getRotationMatrix2D(centro_imagem, 180, 1.0)
	imagem_rotacionada = cv2.warpAffine(imagem, matriz_imagem, (largura, altura))
	return imagem_rotacionada

# Loop
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor imagem	
	imagem = frame.array

	imagem = rotaciona_imagem(imagem)

	regiao_de_interesse()

	# Convertendo padrao de cores da imagem
	imagem_bgr = imagem

	imagem_rgb = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)
	


	# Apresentacao da imagem
	cv2.namedWindow("BGR", cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow("BGR", 50, 100);
	cv2.resizeWindow("BGR", 480, 320)
	cv2.imshow("BGR", imagem_bgr)

	#cv2.namedWindow("RGB", cv2.WINDOW_KEEPRATIO);
	#cv2.moveWindow("RGB", 550, 100);
	#cv2.resizeWindow("RGB", 480, 320)
	#cv2.imshow("RGB", imagem_rgb)


	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'Esc' encerra execucao
	if cv2.waitKey(1) & 0xFF == 27:
		break
cv2.destroyAllWindows()
