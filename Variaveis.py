#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Variaveis

# --------------------------------------------------------

# --------------- Variveis dos Motores -------------------
# Velocidade Geral
velocidade = 20

vel_correcao_dir = 5
vel_correcao_esq = 5

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
limite_ft_dir_extrem = 21000
limite_ft_dir_centro = 21000
limite_ft_esq_centro = 21000
limite_ft_esq_extrem = 21000


limite_obstaculo_incial = 150
limite_obstaculo_final = 200

# --------------------------------------------------------


# ------------- Variveis Imagens e Tela ------------------
# Tamanho Tela
tam_tela_x = 720
tam_tela_y = 580

# Taxa de quadros por segundo
taxa_quadros = 32 
# --------------------------------------------------------


