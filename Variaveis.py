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
velNormal = 16

CONST_CORREC_REF = 1.85
CONST_CORREC_INV = 1.70

velReacao = 23
velVisao = 19
velEmergencia = 20
# --------------------------------------------------------


# ----------------- Variaveis Tempo ----------------------
tempoEsperaPlacaPare = 13
tempoReacaoPlacaPedestre = 26
tempoEsperaPlacaPesdestre = 2

# --------------------------------------------------------


# -------------- Contantes dos Sensores ------------------
# Constantes para atuação dos fototransistores
CONST_A0 = 4500
CONST_A1 = 4500
CONST_A2 = 45
CONST_A3 = 30

CONST_B0 = 4500
CONST_B1 = 4500
CONST_B2 = 30
CONST_B3 = 30


# Constantes Deteccao Obstaculos VL530X
CONST_OBSTAC = 150

# --------------------------------------------------------


# ------------- Variaveis Imagens e Tela ------------------
# Tamanho Tela
tam_original_tela_x, tam_original_tela_y = 840, 680

tam_mini_tela_x, tam_mini_tela_y = 460, 300

# Taxa de quadros por segundo
taxa_quadros = 32

cor_branco = (255, 255, 255)
cor_preto = (0, 0, 0)
cor_vermelho = (0, 0, 255)
cor_verde = (0, 255, 0)
cor_azul = (255, 0, 0)
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
x1_img_sinalizacao_dir, x2_img_sinalizacao_dir = 572, 840
y1_img_sinalizacao_dir, y2_img_sinalizacao_dir = 190, 570

x1_img_sinalizacao_esq, x2_img_sinalizacao_esq = 0, 268
y1_img_sinalizacao_esq, y2_img_sinalizacao_esq = 190, 570


# Area para detecção imagem de obstaculos
x1_img_obs, x2_img_obs = 250, 840
y1_img_obs, y2_img_obs = 550, 670 


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




# --------------- Variaveis Obstaculos -------------------
tresh_min_obs, tresh_max_obs = 150, 240

pt_obstaculo_1, pt_obstaculo_2, pt_obstaculo_3, pt_obstaculo_4 = (105,505), (725,505), (0,680), (840,680)

pontos_obstaculos = np.float32([[pt_obstaculo_1], [pt_obstaculo_2], [pt_obstaculo_3], [pt_obstaculo_4]])
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

# Tempo de espera [ 12 = 5 segundos reais] 
CONST_TEMPO_ESPERA = 12
# --------------------------------------------------------




# ---------------- Variaveis HSV -------------------------
area_min, area_max = 4000, 50000

nome_placa_verde = ""
min_H_v = 33 
max_H_v = 92
min_S_v = 31
max_S_v = 220
min_V_v = 92 
max_V_v = 230

placa_verde = [min_H_v, max_H_v, min_S_v, max_S_v, min_V_v, max_V_v]


nome_check_1 = "Museu."
min_H_ck1 = 126 
max_H_ck1 = 151
min_S_ck1 = 70
max_S_ck1 = 180
min_V_ck1 = 77 
max_V_ck1 = 255

placa_check_1 = [min_H_ck1, max_H_ck1, min_S_ck1, max_S_ck1, min_V_ck1, max_V_ck1]

nome_check_2 = "Igreja."
min_H_ck2 = 9 
max_H_ck2 = 84
min_S_ck2 = 101
max_S_ck2 = 255 
min_V_ck2 = 131 
max_V_ck2 = 255

placa_check_2 = [min_H_ck2, max_H_ck2, min_S_ck2, max_S_ck2, min_V_ck2, max_V_ck2]

nome_check_3 = "Teatro."
min_H_ck3 = 82 
max_H_ck3 = 111
min_S_ck3 = 49 
max_S_ck3 = 255 
min_V_ck3 = 85 
max_V_ck3 = 255

placa_check_3 = [min_H_ck3, max_H_ck3, min_S_ck3, max_S_ck3, min_V_ck3, max_V_ck3]


dados_hsv = [
				(nome_check_1, placa_check_1),
				(nome_check_2, placa_check_2),
				(nome_check_3, placa_check_3)	
			]



nome_semaforo_verde = "Sinal Verde"
min_H_sem_verde = 56 
max_H_sem_verde = 75
min_S_sem_verde = 140 
max_S_sem_verde = 255 
min_V_sem_verde = 75 
max_V_sem_verde = 255


semaforo_verde = [min_H_sem_verde, max_H_sem_verde, min_S_sem_verde, max_S_sem_verde, min_V_sem_verde, max_V_sem_verde]


nome_semaforo_vermelho = "Sinal Vermelho"
min_H_sem_vermelho = 0 
max_H_sem_vermelho = 179
min_S_sem_vermelho = 132
max_S_sem_vermelho = 255
min_V_sem_vermelho = 208 
max_V_sem_vermelho = 255


semaforo_vermelho = [min_H_sem_vermelho, max_H_sem_vermelho, min_S_sem_vermelho, max_S_sem_vermelho, min_V_sem_vermelho, max_V_sem_vermelho]


dados_semaforo = [
					(nome_semaforo_verde, semaforo_verde),
					(nome_semaforo_vermelho, semaforo_vermelho)
				 ]
	
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







