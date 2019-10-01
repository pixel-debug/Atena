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


# ##################### FUNCAO PARA DEFINICAO DOS COMANDOS DO ROBO ##############################
def definicao_de_comandos(status_a0, status_a1, status_a2, status_a3, status_b0, status_b1, status_b2, status_b3, status_visao_faixa_dir, status_visao_faixa_esq, status_obstaculo_vl53x):
	MOVIMENTO_FRENTE = False

	CORRECAO_MOTOR_DIR_VISAO = False
	CORRECAO_MOTOR_ESQ_VISAO = False

	DETECCAO_OBSTACULOS_VISAO = False

	# Condicao para o robo ter movimento liberado
	if(
		  (status_a0 is False) and 
		  (status_a1 is False) and 
		  (status_a2 is False) and 
		  (status_a3 is False) and
		  (status_b0 is False) and 
		  (status_b1 is False) and 
		  (status_b2 is False) and 
		  (status_b3 is False) and  
		  (status_visao_faixa_dir is False) and 
		  (status_visao_faixa_esq is False) and
		  (status_obstaculo_vl53x is False)
	  ):
		MOVIMENTO_FRENTE = True	
	 
	# Condicao para o robo fazer a correcao para a direita a partir da visao
	if(status_visao_faixa_dir is True):
		CORRECAO_MOTOR_DIR_VISAO = True

	# Condicao para o robo fazer a correcao para a esquerda a partir da visao
	if(status_visao_faixa_esq is True):
		CORRECAO_MOTOR_ESQ_VISAO = True



	'''
	# Condicao para o robo fazer a verificacao de obstaculos a partir da visao
	if(
	  (status_visao_faixa_dir is False) and 
	  (status_visao_faixa_esq is False) and
	  (status_anormalidade_faixa_dir is False) and
	  (status_anormalidade_faixa_esq is False)
	  ):
		DETECCAO_OBSTACULOS_VISAO = status_obstaculo_visao
	else:
		DETECCAO_OBSTACULOS_VISAO = False
	
	# --------------------------------------------------------------------------------
	'''

	COMANDOS = [
					MOVIMENTO_FRENTE,
					CORRECAO_MOTOR_DIR_VISAO,
					CORRECAO_MOTOR_ESQ_VISAO,
					DETECCAO_OBSTACULOS_VISAO,
			   ]

	return COMANDOS

# ###############################################################################################



# ##################### FUNCAO PARA GERENCIAR MOVIMENTO E CORRECAO ##############################
def movimento_frente(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq):
	motor.movimento_frente(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq)

def correcao_motor_esq(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq):
	motor.movimento_direita(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq)

def correcao_motor_dir(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq):
	motor.movimento_esquerda(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq)
# ###############################################################################################



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
			if(b <= var.CONST_FT_DIR_SUP and c <= var.CONST_FT_ESQ_SUP):
				break
			elif(a <= var.CONST_ft_dir_sup and d <= var.CONST_FT_ESQ_SUP):
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


# ######################## FUNCAO PARA GERENCIAR ACAO PLACA DESVIO ##############################
def placa_desvio(ctr_vel_motor_dir, ctr_vel_motor_esq):
	print("Detectou Placa Desvio!")
# ###############################################################################################

def analise_matriz_imagem(img):
	soma_matriz = 0
	for i in sum(np.array(img)): 
		soma_matriz += i 
	return soma_matriz

