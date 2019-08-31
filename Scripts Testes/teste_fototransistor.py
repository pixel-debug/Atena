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

# 1º valor raw e 2º valor da tensão
while True:
    print("Fototransistor Direita: {:>5}\t{:>5.3f} \tFototransistor Esquerda: {:>5}\t{:>5.3f}".format(fototransistor_dir.value, fototransistor_dir.voltage, fototransistor_esq.value, fototransistor_esq.voltage))
    time.sleep(0.5)
