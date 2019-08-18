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

ponto_pista_1, ponto_pista_2, ponto_pista_3, ponto_pista_4 = (45,208), (258,208), (26,235), (279,235), 
ponto_destino_1, ponto_destino_2, ponto_destino_3, ponto_destino_4 = (95,0), (220,0), (95,240), (220,240),

pontos_pista = np.float32([[ponto_pista_1], [ponto_pista_2], [ponto_pista_3], [ponto_pista_4]])
pontos_destino = np.float32([[ponto_destino_1], [ponto_destino_2], [ponto_destino_3], [ponto_destino_4]])

# Funcao para regiao de interesse
def regiao_de_interesse(rg_imagem, pontos_pista, pontos_destino):
	cv2.line(rg_imagem, ponto_pista_1, ponto_pista_2, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_1, ponto_pista_3, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_2, ponto_pista_4, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_3, ponto_pista_4, (0,0,255), 2)

	cv2.line(rg_imagem, ponto_destino_1, ponto_destino_2, (0,255,0), 2)
	cv2.line(rg_imagem, ponto_destino_1, ponto_destino_3, (0,255,0), 2)
	cv2.line(rg_imagem, ponto_destino_2, ponto_destino_4, (0,255,0), 2)
	cv2.line(rg_imagem, ponto_destino_3, ponto_destino_4, (0,255,0), 2)

	matriz = cv2.getPerspectiveTransform(pontos_pista, pontos_destino)

	rg_imagem = cv2.warpPerspective(rg_imagem, matriz, (350,240))

	return rg_imagem

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

	imagem_perspectiva = imagem

	imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

	imagem_perspectiva = regiao_de_interesse(imagem_perspectiva, pontos_pista, pontos_destino)

	# Convertendo padrao de cores da imagem
	#imagem_rgb = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)
	
	# Apresentacao da imagem
	cv2.namedWindow("Imagem Original", cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow("Imagem Original", 50, 100);
	cv2.resizeWindow("Imagem Original", 480, 320)
	cv2.imshow("Imagem Original", imagem)

	cv2.namedWindow("Perspectiva Pista", cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow("Perspectiva Pista", 550, 100);
	cv2.resizeWindow("Perspectiva Pista", 480, 320)
	cv2.imshow("Perspectiva Pista", imagem_perspectiva)

	cv2.namedWindow("Imagem Cinza", cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow("Imagem Cinza", 550, 100);
	cv2.resizeWindow("Imagem Cinza", 480, 320)
	cv2.imshow("Imagem Cinza", imagem_cinza)


	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'Esc' encerra execucao
	if cv2.waitKey(1) & 0xFF == 27:
		break
cv2.destroyAllWindows()
