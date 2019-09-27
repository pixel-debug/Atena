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
