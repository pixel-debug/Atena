#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Tratamento

# --------------------------------------------------------

import Variaveis as var
import Motores as motor
import time
import Pista as pista
import Placas as placa
import Tela as tela
import cv2
import RPi.GPIO as GPIO
import Sensores as sensor
import Placas as placa
import Interface as interface
import numpy as np
import Obstaculos as obstaculo


# ########################### FUNCAO DE TRATAMENTO DA INTERFACE MENU ###############################
def interface_menu(op):
	inicializacao, destino_igreja, destino_teatro, destino_museu = False, False, False, False

	if(op == 1):
		nome = "Igreja"
	elif(op == 2):
		nome = "Teatro"
	elif(op == 3):
		nome = "Museu"
	else:
		print("bost")
	
	confir = interface.confirma_opcao(op, nome)

	if(op == 1) and (confir == 1):
		destino_igreja = True
		inicializacao = True
	elif(op == 2) and (confir == 1):
		destino_teatro = True
		inicializacao = True
	elif(op == 3) and (confir == 1):
		destino_museu = True
		inicializacao = True
	
	return inicializacao, destino_igreja, destino_teatro, destino_museu
# ###############################################################################################



# ############################## FUNCAO DE DETECCAO DAS FAIXAS ###################################
def deteccao_faixas_pista(img, ft_dir_inf, ft_dir_sup, ft_esq_sup, ft_esq_inf):

	# ------------- Variaveis que irao definir o status de deteccao das faixas -------------------
	status_foto_dir_inf, status_foto_esq_inf = False, False 
	status_foto_dir_sup, status_foto_esq_sup = False, False

	status_visao_faixa_dir, status_visao_faixa_esq = False, False

	status_normalidade_faixa_dir, status_normalidade_faixa_esq = False, False
	# --------------------------------------------------------------------------------------------


	# --------------- Manipulacao da imagem original para deteccao das faixas --------------------
	img_perspectiva_pista = pista.perspectiva_pista(img)
	img_filtros = pista.filtros_faixas(img_perspectiva_pista) 

	img_faixa_esq = img_filtros[var.y1_faixa_esq:var.y2_faixa_esq, var.x1_faixa_esq:var.x2_faixa_esq]
	img_faixa_esq, cx_esq = pista.detecta_faixas(img_faixa_esq)

	img_faixa_dir = img_filtros[var.y1_faixa_dir:var.y2_faixa_dir, var.x1_faixa_dir:var.x2_faixa_dir]
	img_faixa_dir, cx_dir = pista.detecta_faixas(img_faixa_dir)
	# --------------------------------------------------------------------------------------------


	# -------------- Verificação da deteccao das faixas com os fototransistores ------------------
	if (ft_dir_inf <= var.CONST_FT_DIR_INF):
		status_foto_dir_inf = True
	if (ft_dir_sup <= var.CONST_FT_DIR_SUP):
		status_foto_dir_sup = True
	if (ft_esq_sup <= var.CONST_FT_ESQ_SUP):
		status_foto_esq_sup = True
	if (ft_esq_inf <= var.CONST_FT_ESQ_INF):
		status_foto_esq_inf = True
	# --------------------------------------------------------------------------------------------


	# ------------- Verificação do status de normalidade na detecção das faixas ------------------
	if((cx_dir >= 25) and (cx_dir <= 55)):
		status_normalidade_faixa_dir = True

	if((cx_esq >= 63) and (cx_esq <= 93)):
		status_normalidade_faixa_esq = True

	if(status_normalidade_faixa_dir is True):
		status_dir = "Normal"
	else:
		status_dir = "ANORMAL"

	if(status_normalidade_faixa_esq is True):
		status_esq = "Normal"
	else:
		status_esq = "ANORMAL"
	# --------------------------------------------------------------------------------------------

	# --------------------------- Detecção das faixas com Visao ----------------------------------
	if cx_dir >= 70:
		status_visao_faixa_dir = True

	if cx_esq <= 45:
		status_visao_faixa_esq = True
	# --------------------------------------------------------------------------------------------
	
	#print("Faixa Esq: {0} {1} \tFaixa Dir: {2} {3}".format(status_esq, cx_esq, status_dir, cx_dir))

	retorno = [
				img_perspectiva_pista, 
				img_faixa_esq, 
				img_faixa_dir, 
				status_foto_dir_inf, 
				status_foto_dir_sup, 
				status_foto_esq_sup, 
				status_foto_esq_inf, 
				status_visao_faixa_dir, 
				status_visao_faixa_esq, 
				status_normalidade_faixa_dir, 
				status_normalidade_faixa_esq
              ]

	return retorno
# ###############################################################################################



# ####################### FUNCAO DE TRATAMENTO DE DETECCAO DOS OBSTACULOS #######################
def deteccao_obstaculo(img, distancia_obstaculo):

	# ------------- Variaveis que irao definir o status de deteccao de obstaculos ----------------
	status_obstaculo_visao = False
	status_obstaculo_vl53x = False
	# --------------------------------------------------------------------------------------------

	# --------------------------- Detecção das faixas com Visao ----------------------------------
	img_perspectiva_obstaculos = obstaculo.perspectiva_obstaculo(img)	

	img_filtros_obs = obstaculo.filtros_obstaculos(img_perspectiva_obstaculos) 

	somatorio_matriz = obstaculo.detecta_obstaculos(img_filtros_obs)

	if(somatorio_matriz > 6000):
		status_obstaculo_visao = True
	# --------------------------------------------------------------------------------------------


	# --------------------------- Detecção das faixas com VL53X ----------------------------------
	if((distancia_obstaculo > 0) and (distancia_obstaculo <= var.CONST_OBSTAC)):
		status_obstaculo_vl53x = True
	# --------------------------------------------------------------------------------------------

	sensor.aciona_buzina(status_obstaculo_vl53x)

	print("\nDetectou Obstaculo: {0} \tValor: {1}".format(status_obstaculo_visao, somatorio_matriz))

	retorno = [
				img_filtros_obs,
				status_obstaculo_visao, 
				status_obstaculo_vl53x
			  ]	
	
	return retorno
# ###############################################################################################



# ######################## FUNCAO DE TRATAMENTO DA DETECCAO DAS PLACAS ##########################
def deteccao_placas(img):
	detectou_plc_pare, detectou_plc_pedestre, detectou_plc_desvio = False, False, False 
		
	img_area_detecao_placa = img[var.y1_img_placas_dir:var.y2_img_placas_dir, var.x1_img_placas_dir:var.x2_img_placas_dir]

	detectou_placa, nome_placa, distancia_placa = placa.detecta_placa(img_area_detecao_placa, var.classificadores)
	
	if nome_placa == var.nome_p1 and (distancia_placa > 15 and distancia_placa <= 20):
		detectou_plc_pare = True
	elif nome_placa == var.nome_p2:
		detectou_plc_desvio = True
	elif nome_placa == var.nome_p3 and (distancia_placa > 9 and distancia_placa <= 17):
		detectou_plc_pedestre = True
	
	img = img_area_detecao_placa
	return img, detectou_plc_pare, detectou_plc_pedestre, detectou_plc_desvio
# ###############################################################################################


def placa_pare(ctr_vel_motor_dir, ctr_vel_motor_esq):
	tempoPare = 0
	print("Detectou Placa Pare...")	
	motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
	time.sleep(4)
	while(tempoPare <= var.tempoEsperaPlacaPare):
		print("Andar ate nao ver placa pare")
		motor.movimento_frente(var.velReacao, ctr_vel_motor_dir, ctr_vel_motor_esq)
		tempoPare += 1
	print("Saiu da placa pare")
	
	


def placa_pedestre(ctr_vel_motor_dir, ctr_vel_motor_esq):
	DETECCAO_FAIXA_PEDESTRE = False
	deteccao_obstaculo = False
	tempoPedestre = 0
	print("Detectou Placa Pedestre! Andar cuidadosamente.")	
	while(deteccao_obstaculo is not True):	
		while(DETECCAO_FAIXA_PEDESTRE is not True):
			a, b, c, d = sensor.fototransistores()
			motor.movimento_frente(var.velNormal+2, ctr_vel_motor_dir, ctr_vel_motor_esq)			
			if(b <= var.CONST_ft_dir_sup and c <= var.CONST_ft_esq_sup):
				break
			elif(a <= var.CONST_ft_dir_sup and d <= var.CONST_ft_esq_sup):
				break

		print("Chegou na Faixa! Aguarda 5 segundos...")
		motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
		time.sleep(5)

		print("Verifica ausencia de pedestre...")
		if(deteccao_obstaculo is False):
			print("pode continuar...")
			while(tempoPedestre <= var.tempoReacaoPlacaPedestre):
				motor.movimento_frente(var.velReacao, ctr_vel_motor_dir, ctr_vel_motor_esq)
				tempoPedestre += 1
			break
			
		else:
			print("presença de obstaculo confirmada...")
			motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
		






