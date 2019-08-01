#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Configurações

# --------------------------------------------------------

import RPi.GPIO as GPIO
import Variaveis as var

class Configuracoes:

	def configuracoes():
		GPIO.setup(var.pin_pwm_motor_direita, GPIO.OUT)
		GPIO.setup(var.pin_motor_direita_frente, GPIO.OUT)	
		GPIO.setup(var.pin_motor_direita_tras, GPIO.OUT)


