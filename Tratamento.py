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
import Placas as placa
import Tela as tela


def deteccao_faixas_pista(img):
	detectou_faixa_dir, detectou_faixa_centro, detectou_faixa_esq = False, False, False	
	img_perspectiva_pista = pista.perspectiva_pista(img)
	img_filtros = pista.aplicacao_filtros(img_perspectiva_pista) 

	img_faixa_esq = img_filtros[var.y1_faixa_esq:var.y2_faixa_esq, var.x1_faixa_esq:var.x2_faixa_esq]
	img_faixa_esq, cx_esq = pista.detecta_faixas(img_faixa_esq)

	img_faixa_dir = img_filtros[var.y1_faixa_dir:var.y2_faixa_dir, var.x1_faixa_dir:var.x2_faixa_dir]
	img_faixa_dir, cx_dir = pista.detecta_faixas(img_faixa_dir)

	#tela.apresenta("Imagem Perspe", img_perspectiva_pista, 500, 10)
	#tela.apresenta("Imagem Faixa Esquerda", img_faixa_esq, 10, 400)
	#tela.apresenta("Imagem Faixa Direita", img_faixa_dir, 500, 400)
	if cx_dir >= 50:
		detectou_faixa_dir = True
	elif cx_esq <= 35:
		detectou_faixa_esq = True
	return detectou_faixa_dir, detectou_faixa_centro, detectou_faixa_esq


'''
def deteccao_faixas_pista(ft_dir_extrem, ft_dir_centro, ft_esq_centro, ft_esq_extrem):
	detectou_faixa_dir, detectou_faixa_centro, detectou_faixa_esq = False, False, False	
	if (ft_dir_extrem < var.limite_ft_dir_extrem):
		detectou_faixa_dir = True
	#elif ((ft_dir_centro < var.limite_ft_dir_centro) and (ft_esq_centro < var.limite_ft_esq_centro)):
	#	detectou_faixa_centro = True
	elif (ft_esq_extrem < var.limite_ft_esq_extrem):
		detectou_faixa_esq = True
	return detectou_faixa_dir, detectou_faixa_centro, detectou_faixa_esq
'''

def deteccao_obstaculo(distancia_obstaculo):
	if((distancia_obstaculo >= var.limite_obstaculo_incial) and (distancia_obstaculo <= var.limite_obstaculo_final)):
		detectou_obstaculo = True
	else:
		detectou_obstaculo = False
	return detectou_obstaculo


def deteccao_placa(img):
	img_reigao_placa = img[var.y1_img_placas_dir:var.y2_img_placas_dir, var.x1_img_placas_dir:var.x2_img_placas_dir]
	
	
		   
