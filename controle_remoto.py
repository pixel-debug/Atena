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
import Variaveis as var
import time

import pygame, sys
from pygame.locals import *

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

controle_velocidade_direita = GPIO.PWM(var.pin_ENA, 500)
controle_velocidade_direita.start(0)

controle_velocidade_esquerda = GPIO.PWM(var.pin_ENB, 500)
controle_velocidade_esquerda.start(0)

pygame.init()

screen = pygame.display.set_mode((400,200))
clock = pygame.time.Clock()

class Controle_Remoto:
	try:
		while (True):


	finally:
		print("Cleaning up")
		GPIO.cleanup()

