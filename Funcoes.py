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
	GPIO.output(var.pin_BOZINA, True)
	time.sleep(0.2)
	GPIO.output(var.pin_BOZINA, False)
	time.sleep(0.1)
	GPIO.output(var.pin_BOZINA, True)
	time.sleep(0.4)
	GPIO.output(var.pin_BOZINA, False)
	time.sleep(0.2)

def correcao_fototransistor(pin_FOTOTRANSISTOR_DIR, pin_FOTOTRANSISTOR_ESQ):
	if (GPIO.input(pin_FOTOTRANSISTOR_DIR) == GPIO.LOW and GPIO.input(pin_FOTOTRANSISTOR_ESQ) == GPIO.LOW):
		print("frente.")
	elif GPIO.input(pin_FOTOTRANSISTOR_DIR) == GPIO.HIGH and GPIO.input(pin_FOTOTRANSISTOR_ESQ) == GPIO.LOW:
		print("Direito Branco.")
	elif GPIO.input(pin_FOTOTRANSISTOR_DIR) == GPIO.LOW and GPIO.input(pin_FOTOTRANSISTOR_ESQ) == GPIO.HIGH:
		print("Esquerdo Branco.")
	else:
		print("Contencao.")

	time.sleep(1)
	
