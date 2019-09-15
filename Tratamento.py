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

import Pista as pista
#import Placas as placa
import Tela as tela
import cv2
import RPi.GPIO as GPIO
import Sensores as sensor


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

	
	if (ft_dir_ext < var.CONST_FT_DIR_EXT):
		ft_detectou_faixa_dir_ext = True

	elif (ft_dir_cen < var.CONST_FT_DIR_CEN):
		ft_detectou_faixa_dir_cen = True

	elif (ft_esq_cen < var.CONST_FT_ESQ_CEN):
		ft_detectou_faixa_esq_cen = True

	elif (ft_esq_ext < var.CONST_FT_ESQ_EXT):
		ft_detectou_faixa_esq_ext = True

	if cx_dir >= 70:
		vs_detectou_faixa_dir_ext = True
	if cx_esq <= 45:
		vs_detectou_faixa_esq_ext = True

	tela.apresenta("Imagem Original", img, 10, 10)
	tela.apresenta("Imagem Perspe", img_perspectiva_pista, 500, 10)
	tela.apresenta("Imagem Faixa Esquerda", img_faixa_esq, 10, 400)
	tela.apresenta("Imagem Faixa Direita", img_faixa_dir, 500, 400)
	
	print(cx_esq, cx_dir)
	
	return ft_detectou_faixa_dir_ext, ft_detectou_faixa_dir_cen, ft_detectou_faixa_esq_cen, ft_detectou_faixa_esq_ext, vs_detectou_faixa_dir_ext, vs_detectou_faixa_esq_ext



def deteccao_obstaculo(distancia_obstaculo):
	detectou_obstaculo = False
	if((distancia_obstaculo >= var.CONST_OBSTAC_INI) and (distancia_obstaculo <= var.CONST_OBSTAC_FIM)):
		detectou_obstaculo = True
	
	sensor.aciona_buzina(detectou_obstaculo)
		
	return detectou_obstaculo



   
