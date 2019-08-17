#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Teste de Detecção da Pista

# --------------------------------------------------------

# Processos:
# 1º Conversão da imagem para escala de cinza
# 2º Aplicação do Gaussiano Blur
# 3º Aplicação do Canny para polarizar as cores da imagem. Distingue entre preto e branco
# 4º Buscando região de interesse da imagem

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# Inicializacao da camera e parâmetros de resolucao e quadros por segundo capturado
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)


def faz_coordenadas(imagem, parametros_linha):
	inclinacao, intersecao = parametros_linha
	y1 = imagem.shape[0]
	y2 = int(y1*(3/5))
	x1 = int((y1 - intersecao)/inclinacao)
	x2 = int((y2 - intersecao)/inclinacao)
	return np.array([x1, y1, x2, y2])	

def media_intersecao_linhas(imagem, linhas):
	linha_esquerda = []
	linha_direita = []
	for linha in linhas:
		x1, y1, x2, y2 = linha.reshape(4)
		parametros = np.polyfit((x1, x2), (y1, y2), 1)
		inclinacao = parametros[0]
		intersecao = parametros[1]
		if inclinacao < 0:
			linha_esquerda.append((inclinacao, intersecao))
		else:
			linha_direita.append((inclinacao, intersecao))
	linha_esquerda_media = np.average(linha_esquerda, axis=0)
	linha_direita_media = np.average(linha_direita, axis=0)
	linha_esquerda = faz_coordenadas(imagem, linha_esquerda_media)
	linha_direita = faz_coordenadas(imagem, linha_direita_media)
	return np.array([linha_esquerda, linha_direita])



def cinza(imagem):
	imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
	return imagem_cinza

def blur(imagem):
	imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
	imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0) 
	return imagem_blur

def canny(imagem):
	imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
	imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0) 
	imagem_canny = cv2.Canny(imagem_blur, 50, 150)
	return imagem_canny

def apresenta_linhas(imagem, linhas):
	imagem_linhas = np.zeros_like(imagem)
	if linhas is not None:
		for linha in linhas:
			x1, y1, x2, y2 = linha.reshape(4)
			cv2.line(imagem_linhas, (x1, y1), (x2, y2), (255, 255, 0), 10)
	return imagem_linhas

# Essa função irá determinar uma regição de interesse destanco somente a região onde a pista esta demarcada.
# Ela faz um triangulo que intercepta as duas faixas da pista, esquerda e direita.
# Por fim, todo o resto da imagem, fora do triangulo é definido como preto pois é uma região fora do interesse
def regiao_interesse(imagem):
	altura = imagem.shape[0]
	# Definindo os pontos dos vertices do triangulo
	poligonos = np.array([[(0, altura), (640, altura), (320, 145)]]) 
	mascara = np.zeros_like(imagem) # Definindo como preto todas as outras cores da imagem.
	cv2.fillPoly(mascara, poligonos, 255) # Colore a região de interesse de branco
	mascara_limpa = cv2.bitwise_and(imagem, mascara)	
	return mascara_limpa



for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array	

	#cv2.rectangle(imagem,(0,0),(0+250,0+300),(255,0,0),2)

	# Armazenamento das dimensoes padrao dos frames a serem capturados e criacao do vetor com os pontos centrais da imagem
	(altura, largura) = imagem.shape[:2]
	centro_imagem = (largura / 2, altura / 2)

	# Utilizacao da funcao RotationMatrix2D para realizar a rotacao da imagem a partir do ponto central
	matriz_imagem = cv2.getRotationMatrix2D(centro_imagem, 180, 1.0)

	# Realiza a rotacao da imagem a partir das funcoes determinadas acima
	imagem_rotacionada = cv2.warpAffine(imagem, matriz_imagem, (largura, altura))

	#cv2.line(imagem_rotacionada, (415,2), (415,500), (0,255,0), 10)
	#cv2.line(imagem_rotacionada, (185,2), (185,500), (0,255,0), 10)

	imagem_clone = np.copy(imagem_rotacionada)

	imagem_cinza = cv2.cvtColor(imagem_clone, cv2.COLOR_RGB2GRAY)


	imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0) 

	imagem_canny = cv2.Canny(imagem_blur, 50, 150)

	imagem_interesse = regiao_interesse(imagem_canny)

	linhas = cv2.HoughLinesP(imagem_interesse, 2, np.pi/180, 100, np.array([]),minLineLength=40, maxLineGap=5)

	media_linhas = media_intersecao_linhas(imagem_clone, linhas)

	imagem_linhas = apresenta_linhas(imagem_clone, media_linhas)

	imagem_combo = cv2.addWeighted(imagem_clone, 0.8, imagem_linhas, 1, 1)


	# Apresenta as imagens capturas por meio dos frames
	#cv2.imshow("Streaming Camera Atena", imagem_rotacionada)
	#cv2.imshow("Streaming Camera Atena", imagem_cinza)
	#cv2.imshow("Streaming Camera Atena", imagem_blur)
	#cv2.imshow("Streaming Camera Atena", imagem_canny)
	#cv2.imshow("Streaming Camera Atena", imagem_interesse)
	#cv2.imshow("Streaming Camera Atena", imagem_linhas)
	cv2.imshow("Streaming Camera Atena", imagem_combo)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'q' sai do programa
	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()


