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
velocidade = 11


vel_correcao_dir = 15
vel_correcao_esq = 15
# --------------------------------------------------------


# -------------- Contantes dos Sensores ------------------
# Constantes para atuação dos fototransistores
CONST_FT_DIR_EXT = 22500
CONST_FT_DIR_CEN = 22500
CONST_FT_ESQ_CEN = 22000
CONST_FT_ESQ_EXT = 22000


CONST_OBSTAC_INI = 70
CONST_OBSTAC_FIM = 150

# --------------------------------------------------------


# ------------- Variaveis Imagens e Tela ------------------
# Tamanho Tela
tam_original_tela_x, tam_original_tela_y = 840, 680

tam_mini_tela_x, tam_mini_tela_y = 480, 320

# Taxa de quadros por segundo
taxa_quadros = 32
# --------------------------------------------------------



# ------------- Variaveis das Imagens Filhas -------------
# Area para detecção das faixas
# (155, 215)
# (525, 645)
x1_faixa_esq, x2_faixa_esq = 260, 380
y1_faixa_esq, y2_faixa_esq = 550, 650

# (625, 685)
# (525, 645)
x1_faixa_dir, x2_faixa_dir = 460, 580
y1_faixa_dir, y2_faixa_dir = 550, 650

# Area para detecção das placas
x1_img_placas_dir, x2_img_placas_dir = 572, 830
y1_img_placas_dir, y2_img_placas_dir = 213, 570
# --------------------------------------------------------



# ------------------ Variaveis Pista ---------------------
# Valores para detectar somente as linhas na função inRange
# manha: (150, 255)
# tarde: (200, 240) 
# noite: (90, 125)
tresh_min, tresh_max = 150, 255

canny_min, canny_max = 1000, 1000

# Pontos da imagem Perspectiva da pista
# (45,615), (795,615), (0,680), (840,680)
# (45,505), (795,505), (0,570), (840,570)
pt_pista_1, pt_pista_2, pt_pista_3, pt_pista_4 = (45,505), (795,505), (0,570), (840,570)


pt_destino_1, pt_destino_2, pt_destino_3, pt_destino_4 = (250,0), (590,0), (250,680), (590,680)

pontos_pista = np.float32([[pt_pista_1], [pt_pista_2], [pt_pista_3], [pt_pista_4]])
pontos_destino = np.float32([[pt_destino_1], [pt_destino_2], [pt_destino_3], [pt_destino_4]])

# --------------------------------------------------------


# -------------- Classificadores Placas ------------------
classificador_p1 = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_pare.xml')
nome_p1 = "Pare"

classificador_p2 = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_desvio.xml')
nome_p2 = "Desvio"

classificador_p3 = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_pedestre.xml')
nome_p3 = "Pedestre"

classificadores = 	[
				(nome_p1, classificador_p1), 
				(nome_p2, classificador_p2), 
				(nome_p3, classificador_p3)
					]
# --------------------------------------------------------



# -------------- Constantes das Placas -------------------
# Constantes para distancia de deteccao das placas
CONST_DETECCAO_INI = 11
CONST_DETECCAO_FIM = 15

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







