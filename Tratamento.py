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


def deteccao_faixas_pista(img):
	detectou_faixa_dir, detectou_faixa_centro, detectou_faixa_esq = False, False, False	
	img_perspectiva_pista = pista.perspectiva_pista(img)
	img_filtros = pista.aplicacao_filtros(img_perspectiva_pista) 

	img_faixa_esq = img_filtros[var.y1_faixa_esq:var.y2_faixa_esq, var.x1_faixa_esq:var.x2_faixa_esq]
	img_faixa_esq, cx_esq = pista.detecta_faixas(img_faixa_esq)

	img_faixa_dir = img_filtros[var.y1_faixa_dir:var.y2_faixa_dir, var.x1_faixa_dir:var.x2_faixa_dir]
	img_faixa_dir, cx_dir = pista.detecta_faixas(img_faixa_dir)

	tela.apresenta("Imagem Original", img, 10, 10)
	tela.apresenta("Imagem Perspe", img_perspectiva_pista, 500, 10)
	tela.apresenta("Imagem Faixa Esquerda", img_faixa_esq, 10, 400)
	tela.apresenta("Imagem Faixa Direita", img_faixa_dir, 500, 400)
	if cx_dir >= 50:
		detectou_faixa_dir = True
	elif cx_esq <= 35:
		detectou_faixa_esq = True
	return detectou_faixa_dir, detectou_faixa_centro, detectou_faixa_esq




'''
def deteccao_faixas_pista(ft_dir_ext, ft_dir_cen, ft_esq_cen, ft_esq_ext):
	detectou_faixa_dir_ext, detectou_faixa_dir_cen = False, False 
	detectou_faixa_esq_cen, detectou_faixa_esq_ext = False, False

	if (ft_dir_ext < var.CONST_FT_DIR_EXT):
		detectou_faixa_dir_ext = True

	elif (ft_dir_cen < var.CONST_FT_DIR_CEN):
		detectou_faixa_dir_cen = True

	elif (ft_esq_cen < var.CONST_FT_ESQ_CEN):
		detectou_faixa_esq_cen = True

	elif (ft_esq_ext < var.CONST_FT_ESQ_EXT):
		detectou_faixa_esq_ext = True

	return detectou_faixa_dir_ext, detectou_faixa_dir_cen, detectou_faixa_esq_cen, detectou_faixa_esq_ext
'''			

def deteccao_obstaculo(distancia_obstaculo):
	detectou_obstaculo = False
	if((distancia_obstaculo >= var.CONST_OBSTAC_INI) and (distancia_obstaculo <= var.CONST_OBSTAC_FIM)):
		detectou_obstaculo = True
	
	sensor.aciona_buzina(detectou_obstaculo)
		
	return detectou_obstaculo

'''
def deteccao_placa(img):
	detectou_placa =  False
	
	img_regiao_placas = img[var.y1_img_placas_dir:var.y2_img_placas_dir, var.x1_img_placas_dir:var.x2_img_placas_dir]

	for p in var.classificadores
		nome_placa, distancia_placa = placa.detecta_placas(img_regiao_placas, p)
	
	if (distancia_placa >= 15 and distancia_placa <= 17):
		detectou_placa = True
	
	return detectou_placa
'''


   
