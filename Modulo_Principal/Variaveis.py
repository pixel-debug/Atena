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
velocidade = 40

velReacao = 15

velCorrecaoN1 = 23

velCorrecaoN2 = 24

CONST_CORREC_REF = 1.35
CONST_CORREC_INV = 1.40

velEmergencia = 20

velVisao = 23
# --------------------------------------------------------


# --------------- Variaveis de Tempos --------------------
CONST_TEMPO_PLC_PARE = 12
CONST_TEMPO_PLC_PEDESTRE = 5

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


# ------------- Variaveis Imagens e Tela ------------------
# Tamanho Tela
tam_original_tela_x, tam_original_tela_y = 840, 680

tam_mini_tela_x, tam_mini_tela_y = 460, 300

# Taxa de quadros por segundo
taxa_quadros = 30

cor_branco = (255, 255, 255)
cor_preto = (0, 0, 0)

cor_azul = (0, 0, 255)
cor_azul_fraco = (0, 0, 180)

cor_verde = (0, 255, 0)
cor_verde_fraco = (0, 180, 0)

cor_vermelho = (255, 0, 0)
cor_vermelho_fraco = (180, 0, 0)
# --------------------------------------------------------




# --------------- Variaveis Interface --------------------
tamBotao = 10

tamBotaoIniciar_x = 150
tamBotaoIniciar_y = 35

deslocamento = 50

pos_x_butao_iniciar = 170
pos_y_butao_iniciar = 90

pos_x_butao_sair = 170
pos_y_butao_sair = 140

pos_x_butao_teatro = 525
pos_y_butao_teatro = 311 + deslocamento

pos_x_butao_igreja = 215
pos_y_butao_igreja = 40 + deslocamento

pos_x_butao_museu = 293
pos_y_butao_museu = 469 + deslocamento

tamTela_X_Interface = 740
tamTela_Y_Interface = 507 + deslocamento


tamTela_X_ImgBack = 500
tamTela_y_ImgBack = 600


pos_x_butao_confirma = 170 
pos_y_butao_confirma = 395

pos_x_nega = 170
pos_y_nega = 455

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
y1_img_sinalizacao_dir, y2_img_sinalizacao_dir = 120, 570

x1_img_sinalizacao_esq, x2_img_sinalizacao_esq = 0, 268
y1_img_sinalizacao_esq, y2_img_sinalizacao_esq = 120, 570


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

classificador_p2 = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_pedestre.xml')
nome_p2 = "Pedestre"

classificador_p3 = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_desvio.xml')
nome_p3 = "Desvio"

classificador_p4 = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_60.xml')
nome_p4 = "60 km/h"

classificador_p5 = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_proibido_virar.xml')
nome_p5 = "Proib. Virar"


classificadores_placas_direita = 	[
										(nome_p1, classificador_p1), 
										(nome_p2, classificador_p2), 
										(nome_p3, classificador_p3),
										(nome_p4, classificador_p4),
										(nome_p5, classificador_p5)
									]
# --------------------------------------------------------



# ------------- Classificadores Semaforo -----------------
classificador_semaforo = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_semaforo_verde.xml')
nome_semaforo_verde = "Sinal Aberto"

classificadores_semaforo_verde = 	[
										(nome_semaforo_verde, classificador_semaforo)
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
pin_BUZINA = 22

pin_SETA_FRENTE_DIR = 21
pin_SETA_FRENTE_ESQ = 18

pin_LUZ_FREIO_ESQ = 26
pin_SETA_TRAS_ESQ = 19

pin_LUZ_FREIO_DIR = 17
pin_SETA_TRAS_DIR = 27	
# --------------------------------------------------------







