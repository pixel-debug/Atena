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


# Criação de uma função para destacar a região de interesse na imagem, neste caso irá projetar um triangulo.
def regiao_interesse(imagem):
	altura = imagem.shape[0]
	poligonos = np.array([
	[(200, altura), (1100, altura), (550, 250)]
	]) # Definindo os pontos dos vertices do triangulo
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

'''
plt.imshow(imagem)
plt.show()
plt.imshow(imagem_cinza, cmap="gray")
plt.show()
plt.imshow(imagem_blur, cmap="gray")
plt.show()
'''
plt.imshow(imagem_limpa, cmap="gray")
plt.show()


#cv2.imshow("Resultado",regiao_interesse(imagem_canny))
#cv2.waitKey(0)


