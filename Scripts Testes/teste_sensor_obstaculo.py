#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste Sensor Obstaculo

# --------------------------------------------------------


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

pin_ECHO = 23
pin_TRIG = 24


GPIO.setup(pin_TRIG, GPIO.OUT)
GPIO.setup(pin_ECHO, GPIO.IN)

GPIO.output(pin_TRIG, False)
print("Esperando sensor")
time.sleep(2)
	


