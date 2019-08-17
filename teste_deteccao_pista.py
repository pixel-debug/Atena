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

import cv2
import numpy as np
import matplotlib.pyplot as plt


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

imagem = cv2.imread("Imagens/imagem_teste.jpg")

copia_imagem = np.copy(imagem)

imagem_cinza = cinza(copia_imagem)

imagem_blur = blur(copia_imagem) # Distorce a imagem

imagem_canny = canny(copia_imagem) # A função distingue todas as cores em preto e branco

imagem_limpa = regiao_interesse(imagem_canny)

linhas = cv2.HoughLinesP(imagem_limpa, 2, np.pi/180, 100, np.array([]),minLineLength=40, maxLineGap=5)

media_linhas = media_intersecao_linhas(copia_imagem, linhas)

imagem_linhas = apresenta_linhas(copia_imagem, media_linhas)

imagem_combo = cv2.addWeighted(copia_imagem, 0.8, imagem_linhas, 1, 1) 
'''
plt.imshow(imagem)
plt.show()
plt.imshow(imagem_cinza, cmap="gray")
plt.show()
plt.imshow(imagem_blur, cmap="gray")
plt.show()
plt.imshow(imagem_combo, cmap="gray")
plt.show()
'''
plt.imshow(imagem)
plt.show()


#cv2.imshow("Resultado",regiao_interesse(imagem_canny))
#cv2.waitKey(0)


