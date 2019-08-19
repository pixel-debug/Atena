#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Funcoes

# --------------------------------------------------------

import RPi.GPIO as GPIO
import Variaveis as var
import time

def buzina():
	GPIO.output(var.pin_Bozinha, True)
	time.sleep(0.2)
	GPIO.output(var.pin_Bozinha, False)
	time.sleep(0.1)
	GPIO.output(var.pin_Bozinha, True)
	time.sleep(0.4)
	GPIO.output(var.pin_Bozinha, False)
	time.sleep(0.2)
	
