#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste Fototransitores

# --------------------------------------------------------

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Chamada da interface i2c
i2c = busio.I2C(board.SCL, board.SDA)

# Criando um objeto ADC com a interface i2c
ads = ADS.ADS1115(i2c)

# Criando duas entradas para leitura dos canais 0 e 1 do conversor AD
fototransistor_dir = AnalogIn(ads, ADS.P0)
fototransistor_esq = AnalogIn(ads, ADS.P1)


