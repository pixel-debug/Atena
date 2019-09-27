#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Gerenciador

# --------------------------------------------------------

import cv2
import time
import numpy as np
import Tela as tela
import Pista as pista
import Placas as placa
import Variaveis as var
import Motores as motor
import Sensores as sensor
import Interface as interface
import Obstaculos as obstaculo

# ########################## FUNCAO PARA GERENCIAR ACAO PLACA PARE ##############################
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
# ###############################################################################################



# ###################### FUNCAO PARA GERENCIAR ACAO PLACA PEDESTRE ##############################
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
# ###############################################################################################




def analise_matriz_imagem(img):
	soma_matriz = 0
	for i in sum(np.array(img)): 
		soma_matriz += i 
	return soma_matriz

