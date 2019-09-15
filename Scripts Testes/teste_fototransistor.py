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
ft_dir_extrem = AnalogIn(ads, ADS.P0)
ft_dir_centro = AnalogIn(ads, ADS.P1)
ft_esq_centro = AnalogIn(ads, ADS.P2)
ft_esq_extrem = AnalogIn(ads, ADS.P3)

# 1º valor raw e 2º valor da tensão
while True:
    print("ft_dir_ext: {:>5}\tft_dir_cen: {:>5} \tft_esq_cen: {:>5}\tft_esq_ext: {:>5}".format(ft_dir_extrem.value, ft_dir_centro.value, ft_esq_centro.value, ft_esq_extrem.value))
    time.sleep(0.5)
