#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Motores

# --------------------------------------------------------

import RPi.GPIO as GPIO
import Variaveis as var

def movimento_frente(controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, True)
	GPIO.output(var.pin_IN2, False)
	controle_velocidade_direita.ChangeDutyCycle(var.velocidade)

	GPIO.output(var.pin_IN3, True)
	GPIO.output(var.pin_IN4, False)
	controle_velocidade_esquerda.ChangeDutyCycle(var.velocidade)


def movimento_tras(controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, False)
	GPIO.output(var.pin_IN2, True)
	controle_velocidade_direita.ChangeDutyCycle(var.velocidade)

	GPIO.output(var.pin_IN3, False)
	GPIO.output(var.pin_IN4, True)
	controle_velocidade_esquerda.ChangeDutyCycle(var.velocidade)


def parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, False)
	GPIO.output(var.pin_IN2, False)
	controle_velocidade_direita.ChangeDutyCycle(0)

	GPIO.output(var.pin_IN3, False)
	GPIO.output(var.pin_IN4, False)
	controle_velocidade_esquerda.ChangeDutyCycle(0)


def movimento_direita(controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, True)
	GPIO.output(var.pin_IN2, False)
	controle_velocidade_direita.ChangeDutyCycle(var.velocidade + var.vel_correcao_dir)

	GPIO.output(var.pin_IN3, False)
	GPIO.output(var.pin_IN4, True)
	controle_velocidade_esquerda.ChangeDutyCycle(var.velocidade)


def movimento_esquerda(controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, False)
	GPIO.output(var.pin_IN2, True)
	controle_velocidade_direita.ChangeDutyCycle(var.velocidade)
	GPIO.output(var.pin_IN3, True)
	GPIO.output(var.pin_IN4, False)
	controle_velocidade_esquerda.ChangeDutyCycle(var.velocidade + var.vel_correcao_esq)


