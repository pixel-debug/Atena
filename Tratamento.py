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


def deteccao_faixas_pista(img, ft_dir_ext, ft_dir_cen, ft_esq_cen, ft_esq_ext):
	ft_detectou_faixa_dir_ext, ft_detectou_faixa_esq_ext = False, False 
	ft_detectou_faixa_dir_cen, ft_detectou_faixa_esq_cen = False, False
	vs_detectou_faixa_dir_ext, vs_detectou_faixa_esq_ext = False, False

	img_perspectiva_pista = pista.perspectiva_pista(img)
	img_filtros = pista.aplicacao_filtros(img_perspectiva_pista) 

	img_faixa_esq = img_filtros[var.y1_faixa_esq:var.y2_faixa_esq, var.x1_faixa_esq:var.x2_faixa_esq]
	img_faixa_esq, cx_esq = pista.detecta_faixas(img_faixa_esq)

	img_faixa_dir = img_filtros[var.y1_faixa_dir:var.y2_faixa_dir, var.x1_faixa_dir:var.x2_faixa_dir]
	img_faixa_dir, cx_dir = pista.detecta_faixas(img_faixa_dir)

	
	if (ft_dir_ext <= var.CONST_FT_DIR_EXT):
		ft_detectou_faixa_dir_ext = True

	elif (ft_dir_cen <= var.CONST_FT_DIR_CEN):
		ft_detectou_faixa_dir_cen = True

	elif (ft_esq_cen <= var.CONST_FT_ESQ_CEN):
		ft_detectou_faixa_esq_cen = True

	elif (ft_esq_ext <= var.CONST_FT_ESQ_EXT):
		ft_detectou_faixa_esq_ext = True

	if cx_dir >= 70:
		vs_detectou_faixa_dir_ext = True
	if cx_esq <= 45:
		vs_detectou_faixa_esq_ext = True

	tela.apresenta("Imagem Original", img, 10, 10)
	#tela.apresenta("Imagem Perspe", img_perspectiva_pista, 500, 10)
	tela.apresenta("Imagem Faixa Esquerda", img_faixa_esq, 10, 400)
	tela.apresenta("Imagem Faixa Direita", img_faixa_dir, 500, 400)
	
	#print(cx_esq, cx_dir)
	
	return ft_detectou_faixa_dir_ext, ft_detectou_faixa_dir_cen, ft_detectou_faixa_esq_cen, ft_detectou_faixa_esq_ext, vs_detectou_faixa_dir_ext, vs_detectou_faixa_esq_ext



def deteccao_obstaculo(distancia_obstaculo):
	detectou_obstaculo = False
	if((distancia_obstaculo >= 0) and (distancia_obstaculo <= var.CONST_OBSTAC)):
		detectou_obstaculo = True
	
	sensor.aciona_buzina(detectou_obstaculo)
		
	return detectou_obstaculo



def deteccao_placas(img):
	detectou_plc_pare, detectou_plc_pedestre, detectou_plc_desvio = False, False, False 
		
	img_area_detecao_placa = img[var.y1_img_placas_dir:var.y2_img_placas_dir, var.x1_img_placas_dir:var.x2_img_placas_dir]

	detectou_placa, nome_placa, distancia_placa = placa.detecta_placa(img_area_detecao_placa, var.classificadores)
	
	if nome_placa == var.nome_p1 and (distancia_placa > 17 and distancia_placa <= 19):
		detectou_plc_pare = True
	if nome_placa == var.nome_p2 and (distancia_placa > 17 and distancia_placa <= 19):
		detectou_plc_pedestre = True
	if nome_placa == var.nome_p3:
		detectou_plc_desvio = True

	tela.apresenta("Imagem Placas", img_area_detecao_placa, 500, 10)

	return detectou_plc_pare, detectou_plc_pedestre, detectou_plc_desvio



def placa_pare(cvd, cve):	
	motor.movimento_frente(cvd, cve)
	time.sleep(1)

	print("placa detectada! Aguardando...")
	motor.parar_movimento(cvd, cve)
	time.sleep(4)

	motor.movimento_frente(cvd, cve)
	time.sleep(1)
	#deteccao_placa_pare = False


def placa_pedestre(cvd, cve, dtc_ft_dir_sup, dtc_ft_esq_sup):
	while((dtc_ft_dir_sup is False) and (dtc_ft_esq_sup is False)):	
		motor.movimento_frente(cvd, cve)
		dtc_ft_dir_sup, dtc_ft_esq_sup = True, True
	if((dtc_ft_dir_sup is True) and (dtc_ft_esq_sup is True)):
		motor.parar_movimento(cvd, cve)
		time.sleep(4)
		motor.movimento_frente(cvd, cve)
		time.sleep(1)
	#deteccao_placa_pare = False



