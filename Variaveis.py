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

# --------------- Variveis dos Motores -------------------
# Velocidade Geral
velocidade = 15

vel_correcao_dir =7
vel_correcao_esq = 7

# Motores da Direita
pin_ENA = 12	# PWM motor da direita
pin_IN1 = 20	# Sentido Horário
pin_IN2 = 16	# Sentido Anti-horário

# Motores da Esquerda
pin_ENB = 13	# PWM motor da esquerda
pin_IN3 = 5		# Sentido Horário
pin_IN4 = 6		# Sentido Anti-horário

# --------------------------------------------------------


# -------------- Variveis dos Sensores -------------------
# Bozina
pin_BUZINA = 21

# Constantes para atuação dos fototransistores
limite_ft_dir_extrem = 24000
limite_ft_dir_centro = 24500
limite_ft_esq_centro = 23000
limite_ft_esq_extrem = 22500


limite_obstaculo_incial = 150
limite_obstaculo_final = 200

# --------------------------------------------------------


# ------------- Variveis Imagens e Tela ------------------
# Tamanho Tela
tam_original_tela_x, tam_original_tela_y = 840, 680

tam_mini_tela_x, tam_mini_tela_y = 480, 320

# Taxa de quadros por segundo
taxa_quadros = 32 
# --------------------------------------------------------



# ------------------ Variaveis Pista ---------------------
# Area para detecção das faixas
x1_faixa_esq, x2_faixa_esq = 170, 270
y1_faixa_esq, y2_faixa_esq = 490, 650

x1_faixa_dir, x2_faixa_dir = 530, 630
y1_faixa_dir, y2_faixa_dir = 490, 650


# Valores para detectar somente as linhas na função inRange
# manha: (150, 255)
# tarde: (200, 240) 
# noite: (145, 165)
tresh_min, tresh_max = 150, 255

canny_min, canny_max = 1000, 1000

# Pontos da imagem Perspectiva da pista
pt_pista_1, pt_pista_2, pt_pista_3, pt_pista_4 = (50,570), (750,570), (5,635), (795,635)
pt_destino_1, pt_destino_2, pt_destino_3, pt_destino_4 = (160,0), (640,0), (160,680), (640,680)

pontos_pista = np.float32([[pt_pista_1], [pt_pista_2], [pt_pista_3], [pt_pista_4]])
pontos_destino = np.float32([[pt_destino_1], [pt_destino_2], [pt_destino_3], [pt_destino_4]])


# --------------------------------------------------------


