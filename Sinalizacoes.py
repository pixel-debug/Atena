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
import Variaveis as var

def detecta_placas_direita(img, classificadores):
	deteccao, nome_real, distancia_placa = " - ",  " - ", " - "
	status_pare, status_pedestre, status_desvio =  False, False, False

	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	for c in classificadores:
		nome, classificador = c
		
		img_detecta_placa = classificador.detectMultiScale(img_gray, 1.2, 10)
		
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

		
	return deteccao, nome_real, distancia_placa



def detecta_placas_esquerda(img, classificadores):
	deteccao, nome_real, distancia_placa = " - ",  " - ", " - "
	status_60km, status_virar_esq, status_proibido_virar =  False, False, False

	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	for c in classificadores:
		nome, classificador = c
		
		img_detecta_placa = classificador.detectMultiScale(img_gray, 1.2, 10)
		
		for (x,y,w,h) in img_detecta_placa:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		for (x,y,w,h) in img_detecta_placa:
			distancia_placa = calculo_distancia_placa(x, w)

		for (x,y,w,h) in img_detecta_placa:
			cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			cv2.putText(img, str(distancia_placa)+" cm", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			if nome == var.nome_p1:
				nome_real = nome
				status_60km = True
				deteccao = status_60km
			if nome == var.nome_p2:
				nome_real = nome
				status_virar_esq = True
				deteccao = status_virar_esq
			if nome == var.nome_p3:
				nome_real = nome
				status_proibido_virar = True
				deteccao = status_proibido_virar 

		
	return deteccao, nome_real, distancia_placa


def placas_checkpoints(img, dados_hsv):
	status_ck_1, status_ck_2, status_ck_3, = False, False, False
	img_nova, nome_real, distancia_placa = " - ", " - ",  " - "
	
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	img_clone = img.copy()

	for d in dados_hsv:
		nome, statusores_hsv_checkpoints = d
				
		min_H, max_H, min_S, max_S, min_V, max_V = statusores_hsv_checkpoints
		
		hsv_min = np.array([min_H, min_S, min_V])
		hsv_max = np.array([max_H, max_S, max_V])
	
		mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

		img_resultado = cv2.bitwise_and(img, img, mask=mascara)
	
		_, contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		for c in contours:
			if ((cv2.contourArea(c) > var.area_min) and (cv2.contourArea(c) < var.area_max)):
				x,y,w,h = cv2.boundingRect(c)
				distancia_placa = calculo_distancia_placa(x, w)
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 3)
				cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
				cv2.putText(img, str(distancia_placa)+" cm", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
				img_nova = img[y:(y+h),x:(x+w)]

				if nome == var.nome_check_1:
					nome_real = nome
					status_ck_1 = True

				if nome == var.nome_check_2:
					nome_real = nome
					status_ck_2 = True

				if nome == var.nome_check_3:
					nome_real = nome
					status_ck_3 = True

	return img_nova, nome_real, status_ck_1, status_ck_2, status_ck_3, distancia_placa



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

def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)


