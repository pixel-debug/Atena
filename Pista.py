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

def perspectiva_pista(img, pontos_pista, pontos_destino):
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
	

def aplicacao_filtros(img):
	img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	img_blur = cv2.GaussianBlur(img_cinza,(5,5),0)
	
	# Valores para detectar somente as linhas na função inRange
	# tarde: (200, 240) 
	# noite: (145, 165)
	# Binariza a imagem, definindo regiões pretas e brancas. Para visualizar a imagem binarizada comentar linhas abaixo
	img_tresh = cv2.inRange(img_blur, 145, 205) 

	img_canny = cv2.Canny(img_tresh, 1000, 1000) # Cria contornos especificos nos elementos de cor mais clara. Detecção de bordas.

	img_final = cv2.add(img_tresh, img_canny) # Soma as duas imagens para maior confiabilidade na deteccao das linhas da pista
	
	return img_final

def detecta_faixas(img):
	# Color thresholding
	ret,thresh = cv2.threshold(img,145,205,cv2.THRESH_BINARY_INV)

	# Find the contours of the frame
	_, contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

	if len(contours) > 0:
		c = max(contours, key=cv2.contourArea)

		M = cv2.moments(c)

		cx = int(M['m10']/M['m00'])

		cy = int(M['m01']/M['m00'])

		cv2.line(img,(cx,0),(cx,var.tam_original_tela_y),(255,0,0),1)

		cv2.line(img,(0,cy),(var.tam_original_tela_x,cy),(255,0,0),1)

		cv2.drawContours(img, contours, -1, (0,255,0), 1)

		return img


	

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array

	tela.apresenta("Imagem Original", imagem, 505, 15)

	imagem_perspectiva_pista = perspectiva_pista(imagem, pontos_pista, pontos_destino)
	
	imagem_filtros = aplicacao_filtros(imagem_perspectiva_pista)

	faixa_esq = imagem_filtros[var.y1_faixa_esq:var.y2_faixa_esq, var.x1_faixa_esq:var.x2_faixa_esq]
	faixa_esq = detecta_faixas(faixa_esq)

	faixa_dir = imagem_filtros[var.y1_faixa_dir:var.y2_faixa_dir, var.x1_faixa_dir:var.x2_faixa_dir]
	faixa_dir = detecta_faixas(faixa_dir)


	
	tela.apresenta("Imagem Pista", imagem_perspectiva_pista, 5, 380)
	tela.apresenta("Faixa Esquerda", faixa_esq, 505, 380)
	tela.apresenta("Imagem Direita", faixa_dir, 5, 30)
	
	#cv2.imshow("Streaming Camera Atena", imagem)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'q' sai do programa
	if cv2.waitKey(1) & 0xFF == 27:
		break
	
	

cv2.destroyAllWindows()

