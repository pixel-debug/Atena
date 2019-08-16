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

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread("Imagens/imagem_teste.jpg")

copia_imagem = np.copy(imagem)

imagem_cinza = cv2.cvtColor(copia_imagem, cv2.COLOR_RGB2GRAY)

cv2.imshow("",imagem_cinza)
cv2.waitKey(0)

