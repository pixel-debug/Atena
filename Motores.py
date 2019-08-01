#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

# --------------------------------------------------------

import RPi.GPIO as GPIO
import Variaveis as var

class Motores:

	def movimento_frente(velocidade, controle_velocidade_direita, controle_velocidade_esquerda):
		GPIO.output(var.pin_motor_direita_frente, True)
		GPIO.output(var.pin_motor_direita_tras, False)
		controle_velocidade_direita.ChangeDutyCycle(velocidade)

		GPIO.output(var.pin_motor_esquerda_frente, True)
		GPIO.output(var.pin_motor_esquerda_tras, False)
		controle_velocidade_esquerda.ChangeDutyCycle(velocidade)


	def movimento_tras(velocidade, controle_velocidade_direita, controle_velocidade_esquerda):
		GPIO.output(var.pin_motor_direita_frente, False)
		GPIO.output(var.pin_motor_direita_tras, True)
		controle_velocidade_direita.ChangeDutyCycle(velocidade)

		GPIO.output(var.pin_motor_esquerda_frente, False)
		GPIO.output(var.pin_motor_esquerda_tras, True)
		controle_velocidade_esquerda.ChangeDutyCycle(velocidade)


	def parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda):
		GPIO.output(var.pin_motor_direita_frente, False)
		GPIO.output(var.pin_motor_direita_tras, False)
		controle_velocidade_direita.ChangeDutyCycle(0)

		GPIO.output(var.pin_motor_esquerda_frente, False)
		GPIO.output(var.pin_motor_esquerda_tras, False)
		controle_velocidade_esquerda.ChangeDutyCycle(0)
