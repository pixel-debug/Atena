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
	
GPIO.output(pin_TRIG,True)
time.sleep(0.00001)
GPIO.output(pin_TRIG, False)

while GPIO.input(pin_ECHO) == 0:
	pulse_start = time.time()

while GPIO.input(pin_ECHO) == 1:
	pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distancia:", distance," cm")


GPIO.cleanup()
