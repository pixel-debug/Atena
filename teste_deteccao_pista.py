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
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

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

	# Convertendo padrao de cores da imagem
	imagem_bgr = imagem

	imagem_rgb = cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)

	# Apresentacao da imagem
	cv2.imshow("Teste Deteccao Pista", imagem)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'Esc' encerra execucao
	if cv2.waitKey(1) & 0xFF == 27:
		break
cv2.destroyAllWindows()
