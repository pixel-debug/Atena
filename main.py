#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Main

# --------------------------------------------------------

import RPi.GPIO as GPIO
import Configuracoes as definir
import Motores as motor
import Funcoes as funcao
import Variaveis as var
import time


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

controle_velocidade_direita = GPIO.PWM(var.pin_ENA, 500)
controle_velocidade_direita.start(0)

controle_velocidade_esquerda = GPIO.PWM(var.pin_ENB, 500)
controle_velocidade_esquerda.start(0)

class main:
	try:
		while (True):
			a, b, c, d = funcao.fototransistores()
			print("Fototransistor Direita: {:>5}\t{:>5.3f} \tFototransistor Esquerda: {:>5}\t{:>5.3f}".format(a, b, c, d))
			time.sleep(0.5)
	finally:
		print("Cleaning up")
		GPIO.cleanup()
