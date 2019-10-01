#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Semaforo

# --------------------------------------------------------

import cv2
import Variaveis as var

def detecta_semaforo(img, classificadores):
	nome, distancia_semaforo = "Semáforo", " - "
	estado_vermelho, estado_amarelo, estado_verde =  False, False, False

	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	
	img_detecta_semaforo = classificador.detectMultiScale(img_gray, 1.2, 10)
	
	for (x,y,w,h) in img_detecta_semaforo:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

	for (x,y,w,h) in img_detecta_semaforo:
		distancia_semaforo = calculo_distancia_semaforo(x, w)

	for (x,y,w,h) in img_detecta_semaforo:
		cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
		cv2.putText(img, str(distancia_semaforo)+" cm", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
	if estado == vermelho:
		estado_vermelho = True
	if estado == amarelo:
		estado_amarelo = True
	if estado == verde:
		estado_verde = True


		
	return estado_vermelho, estado_amarelo, estado_verde, distancia_placa


def calculo_distancia_semaforo(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)





