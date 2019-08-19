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

histograma_pista = np.array([])

def histogramas(histograma_pista, img):
	histograma_pista.resize(400, refcheck=False)

	for i in range(400):
		imagem_regiao_hist = cv2.rectangle(imagem, (i,140), (1,240), (0,0,255), 2)
		imagem_dividida = cv2.divide(255, imagem_regiao_hist, imagem_regiao_hist)		
		i += 1		
	return imagem_dividida
		


def limiarizacao(img):
	# Valores para detectar somente as linhas na função inRange
	# tarde: (200, 240) 
	# noite: (145, 165)
	img_tresh = cv2.inRange(img, 145, 165) # Binariza a imagem, definindo regiões pretas e brancas
	img_canny = cv2.Canny(img, 500, 600) # Cria contornos especificos nos elementos de cor mais clara	
	img_final = cv2.add(img_tresh, img_canny) # Soma as duas imagens para maior confiabilidade na deteccao das linhas da pista
	img_final = cv2.cvtColor(img_final, cv2.COLOR_GRAY2RGB)
	return img_final


# Funcao para regiao de interesse
def regiao_de_interesse(rg_imagem, pontos_pista, pontos_destino):
	cv2.line(rg_imagem, ponto_pista_1, ponto_pista_2, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_1, ponto_pista_3, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_2, ponto_pista_4, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_3, ponto_pista_4, (0,0,255), 2)

	# Cria uma matriz a partir dos pontos definidos
	matriz = cv2.getPerspectiveTransform(pontos_pista, pontos_destino)

	#Cria uma nova perspectiva de imagem atraves da definicao da matriz gerada pelos pontos que dermacaram a regiao de interesse
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

	imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

	imagem_cinza = regiao_de_interesse(imagem_cinza, pontos_pista, pontos_destino)

	imagem_perspectiva = regiao_de_interesse(imagem, pontos_pista, pontos_destino)

	imagem_limiarizada = limiarizacao(imagem_cinza)

	#imagem_limiarizada = histogramas(imagem_limiarizada)

	a = histogramas(histograma_pista, imagem)

	
	# Apresentacao das imagens
	cv2.namedWindow("Imagem Original", cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow("Imagem Original", 20, 20);
	cv2.resizeWindow("Imagem Original", 480, 320)
	cv2.imshow("Imagem Original", a)
	'''
	cv2.namedWindow("Perspectiva Pista", cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow("Perspectiva Pista", 520, 20);
	cv2.resizeWindow("Perspectiva Pista", 480, 320)
	cv2.imshow("Perspectiva Pista", imagem_perspectiva)

	cv2.namedWindow("Imagem Cinza", cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow("Imagem Cinza", 20, 360);
	cv2.resizeWindow("Imagem Cinza", 480, 320)
	cv2.imshow("Imagem Cinza", imagem_cinza)

	cv2.namedWindow("Imagem Limiarizada", cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow("Imagem Limiarizada", 520, 360);
	cv2.resizeWindow("Imagem Limiarizada", 480, 320)
	cv2.imshow("Imagem Limiarizada", imagem_limiarizada)
	'''
	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'Esc' encerra execucao
	if cv2.waitKey(1) & 0xFF == 27:
		break
cv2.destroyAllWindows()
