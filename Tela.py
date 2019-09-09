#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Tela

# --------------------------------------------------------

import cv2
import Variaveis as var


def apresenta(nome, imagem, pos_x, pos_y):
	cv2.namedWindow(nome, cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow(nome, pos_x, pos_y);
	cv2.resizeWindow(nome, var.tam_mini_tela_x, var.tam_mini_tela_y)
	cv2.imshow(nome, imagem)
