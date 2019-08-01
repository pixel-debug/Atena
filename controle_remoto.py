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
			clock.tick(30)
			key=pygame.key.get_pressed()
			motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)

			if key[pygame.K_UP]:
				motor.movimento_frente(var.velocidade, controle_velocidade_direita, controle_velocidade_esquerda)	
			if key[pygame.K_RIGHT]:
				motor.movimento_direita(var.velocidade-30, controle_velocidade_direita, controle_velocidade_esquerda)
			if key[pygame.K_LEFT]:
				motor.movimento_esquerda(var.velocidade-30, controle_velocidade_direita, controle_velocidade_esquerda)
			if key[pygame.K_DOWN]:
				motor.movimento_tras(var.velocidade, controle_velocidade_direita, controle_velocidade_esquerda)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()			
	finally:
		print("Cleaning up")
		GPIO.cleanup()

