#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste MOvimentos

# --------------------------------------------------------


import RPi.GPIO as GPIO
import Configuracoes as definir
import Motores as motor
import Variaveis as var
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
