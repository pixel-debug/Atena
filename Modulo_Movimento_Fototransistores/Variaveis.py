#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Variaveis

# --------------------------------------------------------

import numpy as np
import cv2

# --------------- Variaveis dos Motores -------------------
# Velocidade Geral
velNormal = 14

velReacao = 15

velCautela = 12

velCorrecaoN1 = 25

velCorrecaoN2 = 27

CONST_CORREC_REF = 1.35
CONST_CORREC_INV = 1.40

velEmergencia = 20

velVisao = 27
# --------------------------------------------------------



# --------------------------------------------------------

# -------------- Contantes dos Sensores ------------------
# Constantes para atuação dos fototransistores
CONST_A0 = 4500
CONST_A1 = 4500
CONST_A2 = 45
CONST_A3 = 4500

CONST_B0 = 4500
CONST_B1 = 4500
CONST_B2 = 30
CONST_B3 = 4500


# Constantes Deteccao Obstaculos VL530X
CONST_OBSTAC = 150

# --------------------------------------------------------



# --------------- Configuracoes GPIO's -------------------
# Motores da Direita
pin_ENA = 12	# PWM motor da direita
pin_IN1 = 20	# Sentido Horário
pin_IN2 = 16	# Sentido Anti-horário

# Motores da Esquerda
pin_ENB = 13	# PWM motor da esquerda
pin_IN3 = 5		# Sentido Horário
pin_IN4 = 6		# Sentido Anti-horário

# Bozina
pin_BUZINA = 26
# --------------------------------------------------------







