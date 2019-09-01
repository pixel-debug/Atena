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
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def buzina():
	GPIO.output(var.pin_BOZINA, True)
	time.sleep(0.2)
	GPIO.output(var.pin_BOZINA, False)
	time.sleep(0.1)
	GPIO.output(var.pin_BOZINA, True)
	time.sleep(0.4)
	GPIO.output(var.pin_BOZINA, False)
	time.sleep(0.2)


def fototransistores():
	# Chamada da interface i2c
	i2c = busio.I2C(board.SCL, board.SDA)

	# Criando um objeto ADC com a interface i2c
	ads = ADS.ADS1115(i2c)

	# Criando duas entradas para leitura dos canais 0 e 1 do conversor AD
	fototransistor_dir = AnalogIn(ads, ADS.P0)
	fototransistor_esq = AnalogIn(ads, ADS.P1)

	return fototransistor_dir.value, fototransistor_dir.voltage, fototransistor_esq.value, fototransistor_esq.voltage

	
