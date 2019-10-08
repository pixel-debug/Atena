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
import Pista as pista
import Variaveis as var
import Motores as motor
import Sensores as sensor
import Interface as interface
import Obstaculos as obstaculo
import Sinalizacoes as sinalizacao


# ##################### FUNCAO PARA DEFINICAO DOS COMANDOS DO ROBO ##############################
def definicao_de_comandos(status_a0, status_a1, status_a2, status_a3, status_b0, status_b1, status_b2, status_b3, status_visao_faixa_dir, status_visao_faixa_esq, status_faixa_contencao_visao, status_obstaculo_vl53x):
	MOVIMENTO_FRENTE = False

	CORRECAO_MOTOR_DIR_VISAO = False
	CORRECAO_MOTOR_ESQ_VISAO = False

	DETECCAO_OBSTACULOS_VISAO = False

	FAIXA_CONTENCAO = False

	FAIXA_CONTENCAO_VISAO = False
	FAIXA_CONTENCAO_FOTO = False

	# Condicao para o robo ter movimento liberado
	if(
		  
		  (status_a3 is False) and
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

	if(((status_visao_faixa_dir is True) and (status_visao_faixa_esq is True)) or (status_faixa_contencao_visao is True)):	
		FAIXA_CONTENCAO_VISAO = True

	if(
			((status_a0 is True) and (status_b0 is True)) or 
			((status_a1 is True) and (status_b1 is True)) or 
			((status_a3 is True) and (status_b3 is True))  
	  ):
		FAIXA_CONTENCAO_FOTO = True



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
					FAIXA_CONTENCAO_VISAO,
					FAIXA_CONTENCAO_FOTO
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

def interrupcao_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq):
	motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
# ###############################################################################################



# ########################## FUNCAO PARA GERENCIAR ACAO PLACA PARE ##############################
def placa_pare(ctr_vel_motor_dir, ctr_vel_motor_esq):
	print("Detectou Placa Pare...")
	for i in range(100000):	
		motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
	
	print("Andar ate nao ver placa pare")
	for i in range(50000):	
		motor.movimento_frente(var.velReacao, ctr_vel_motor_dir, ctr_vel_motor_esq)
		
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


def semaforo_vermelho(ctr_vel_motor_dir, ctr_vel_motor_esq):
	print("Sinal vermelho!!!")
	SINAL_VERMELHO = True
	while(SINAL_VERMELHO is True):
		_, _, _, a3, _, _, _, b3 = sensor.fototransistores()
		print("Indo ate a faixa de conteção para aguardar...")
		gerencia.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
		if((a3 <= var.CONST_A3) and (b3 <= var.CONST_B3)):
			print("Faixa de contenão")
			motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)	
			SINAL_VERMELHO = False

	print("Aguardando abrir sinal verde!")
	if(status_semaforo_verde is False):
		print("Sinal verde esta fechado!")
		motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)		
		SINAL_VERMELHO = True
				
								
def semaforo_verde(ctr_vel_motor_dir, ctr_vel_motor_esq):			
	print("Sinal verde!!!")
	if((a3 <= var.CONST_A3) and (b3 <= var.CONST_B3)):
		SINAL_VERDE = True
		while(SINAL_VERDE is True):
			_, _, _, a3, _, _, _, b3 = sensor.fototransistores()
			print("Faixa de contenção \tA3:{:>5} B3:{:>5}".format(_, _, _, a3, _, _, _, b3))
			motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)

			if(obstaculo is False):
				print("Sem obstaculo! Prosseguir...")
				gerencia.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)						
	
			if((a3 >= var.CONST_A3) and (b3 >= var.CONST_B3)):
				print("Saiu da faixa de contenção...")
				SINAL_VERDE = False
				#break





def analise_matriz_imagem(img):
	soma_matriz = 0
	for i in sum(np.array(img)): 
		soma_matriz += i 
	return soma_matriz

