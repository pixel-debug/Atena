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

def deteccao_faixas_pista(ft_dir_extrem, ft_dir_centro, ft_esq_centro, ft_esq_extrem):
	detectou_faixa_dir, detectou_faixa_centro, detectou_faixa_esq = False, False, False	
	if (ft_dir_extrem < var.limite_ft_dir_extrem):
		detectou_faixa_dir = True
	elif ((ft_dir_centro < var.limite_ft_dir_centro) and (ft_esq_centro < var.limite_ft_esq_centro)):
		detectou_faixa_centro = True
	elif (ft_esq_extrem < var.limite_ft_esq_extrem):
		detectou_faixa_esq = True
	return detectou_faixa_dir, detectou_faixa_centro, detectou_faixa_esq


def deteccao_obstaculo(distancia_obstaculo):
	if((distancia_obstaculo >= var.limite_obstaculo_incial) and (distancia_obstaculo <= var.limite_obstaculo_final)):
		detectou_obstaculo = True
	else:
		detectou_obstaculo = False
	return detectou_obstaculo
	
	
		   
