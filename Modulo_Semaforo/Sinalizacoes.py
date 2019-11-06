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
import Variaveis_HSV as var_hsv



def hsv_semaforo_vermelho(img, semaforo_vermelho):
	status_vermelho = False
	
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			
	min_H, max_H, min_S, max_S, min_V, max_V = semaforo_vermelho
	
	hsv_min = np.array([min_H, min_S, min_V])
	hsv_max = np.array([max_H, max_S, max_V])

	mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

	img_resultado = cv2.bitwise_and(img, img, mask=mascara)

	_, contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	'''
	for c in contours:
		if ((cv2.contourArea(c) > var_hsv.SEMAFORO_TESTE)):
			print(cv2.contourArea(c))	
	'''
	
	for c in contours:
		if (((cv2.contourArea(c) > var_hsv.CONST_DETECCAO_SEMAFORO_VERMELHO - 500)) and (cv2.contourArea(c) <= (var_hsv.CONST_DETECCAO_SEMAFORO_VERMELHO + 500))):			
			x,y,w,h = cv2.boundingRect(c)
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 3)
			cv2.putText(img, var_hsv.nome_semaforo_vermelho_hsv, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			status_vermelho = True
	
			
	return  status_vermelho





def hsv_semaforo_verde(img, semaforo_verde):
	status_verde = False
	
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		
	min_H, max_H, min_S, max_S, min_V, max_V = semaforo_verde
	
	hsv_min = np.array([min_H, min_S, min_V])
	hsv_max = np.array([max_H, max_S, max_V])

	mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

	img_resultado = cv2.bitwise_and(img, img, mask=mascara)

	_, contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	'''
	for c in contours:
		if ((cv2.contourArea(c) > var_hsv.SEMAFORO_TESTE)):
			print(cv2.contourArea(c))	
	'''

	for c in contours:
		if (((cv2.contourArea(c) > var_hsv.CONST_DETECCAO_SEMAFORO_VERDE - 300)) and (cv2.contourArea(c) <= (var_hsv.CONST_DETECCAO_SEMAFORO_VERDE + 300))):
			x,y,w,h = cv2.boundingRect(c)	
			distancia_placa = calculo_distancia_placa(x, w)
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 3)
			cv2.putText(img, var_hsv.nome_semaforo_verde_hsv, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			status_verde = True
	
	return  status_verde





def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)


