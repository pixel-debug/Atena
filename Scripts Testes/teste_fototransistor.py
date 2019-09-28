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
ads_a = ADS.ADS1115(i2c, address=0x48)
ads_b = ADS.ADS1115(i2c, address=0x49)


# Criando duas entradas para leitura dos canais 0 e 1 do conversor AD
a0 = AnalogIn(ads, ADS.P0)
a1 = AnalogIn(ads, ADS.P1)
a2 = AnalogIn(ads, ADS.P2)
a3 = AnalogIn(ads, ADS.P3)

# 1º valor raw e 2º valor da tensão
while True:
    print("A0:{:>5} \tA1:{:>5} \tA2:{:>5} \tA3:{:>5}".format(a0.value, a1.value, a2.value, a3.value))
    time.sleep(0.5)
