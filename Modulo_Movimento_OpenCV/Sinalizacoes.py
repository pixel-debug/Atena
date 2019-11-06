#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Sinalizacoes

# --------------------------------------------------------
import cv2
import numpy as np
import Variaveis as var

def detecta_placas_direita(img, classificadores):
	deteccao, nome_real, distancia_placa = " - ",  " - ", " - "
	status_pare, status_pedestre, status_desvio =  False, False, False

	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	for c in classificadores:
		nome, classificador = c
		
		img_detecta_placa = classificador.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=10)
		
		for (x,y,w,h) in img_detecta_placa:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		for (x,y,w,h) in img_detecta_placa:
			distancia_placa = calculo_distancia_placa(x, w)

		for (x,y,w,h) in img_detecta_placa:
			cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			cv2.putText(img, str(distancia_placa)+" cm", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			if nome == var.nome_p1:
				nome_real = nome
				status_pare = True
				deteccao = status_pare
			if nome == var.nome_p2:
				nome_real = nome
				status_pedestre = True
				deteccao = status_pedestre
			if nome == var.nome_p3:
				nome_real = nome
				status_desvio = True
				deteccao = status_desvio 

		
	return nome_real, distancia_placa




def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)


