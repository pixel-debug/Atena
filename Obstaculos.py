#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Obstaculos

# --------------------------------------------------------
import cv2
import Variaveis as var


def perspectiva_obstaculo(img):
	cv2.line(img, var.pt_obstaculo_1, var.pt_obstaculo_2, (var.cor_azul), 4)
	cv2.line(img, var.pt_obstaculo_1, var.pt_obstaculo_3, (var.cor_azul), 4)
	cv2.line(img, var.pt_obstaculo_2, var.pt_obstaculo_4, (var.cor_azul), 4)
	cv2.line(img, var.pt_obstaculo_3, var.pt_obstaculo_4, (var.cor_azul), 4)

	cv2.line(img, var.pt_destino_1, var.pt_destino_2, (var.cor_verde), 4)
	cv2.line(img, var.pt_destino_1, var.pt_destino_3, (var.cor_verde), 4)
	cv2.line(img, var.pt_destino_2, var.pt_destino_4, (var.cor_verde), 4)
	cv2.line(img, var.pt_destino_3, var.pt_destino_4, (var.cor_verde), 4)

	matriz = cv2.getPerspectiveTransform(var.pontos_obstaculos, var.pontos_destino)
	img = cv2.warpPerspective(img, matriz, (var.tam_original_tela_x, var.tam_original_tela_y)) 
	return img


def aplicacao_filtros(img):
	img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	img_blur = cv2.GaussianBlur(img_cinza,(5,5),0)

	img_tresh = cv2.inRange(img_blur, var.tresh_min_obs, var.tresh_max_obs) 

	return img_tresh
