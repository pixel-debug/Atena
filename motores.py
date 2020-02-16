#-*- coding utf-8 -*-

# ----------------------- Atena --------------------------

# 	Projeto: Navegação de um robô autônomo educativo 
#            em cenário dinâmico 
# 	Ano: 2020
# 	Orientadora: Natalia Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Motores

# --------------------------------------------------------

import RPi.GPIO as GPIO
from configuracoes import Configuracoes

class Motores():
	
	def __init__(self):
		self.configura = Configuracoes()

	def frente(self, velocidade, controle_motor_dir, controle_motor_esq):
		GPIO.output(self.configura.pin_IN1, True)
		GPIO.output(self.configura.pin_IN2, False)
		controle_motor_dir.ChangeDutyCycle(velocidade)

		GPIO.output(self.configura.pin_IN3, True)
		GPIO.output(self.configura.pin_IN4, False)
		controle_motor_esq.ChangeDutyCycle(velocidade)
	

	def esquerda(velocidade, controle_motor_dir, controle_motor_esq):
		pass

	def direita(velocidade, controle_motor_dir, controle_motor_esq):
		pass

	def tras(self, velocidade, controle_motor_dir, controle_motor_esq):
		GPIO.output(self.configura.pin_IN1, False)
		GPIO.output(self.configura.pin_IN2, True)
		controle_motor_dir.ChangeDutyCycle(velocidade)

		GPIO.output(self.configura.pin_IN3, False)
		GPIO.output(self.configura.pin_IN4, True)
		controle_motor_esq.ChangeDutyCycle(velocidade)

	def parar(self, velocidade, controle_motor_dir, controle_motor_esq):
		GPIO.output(self.configura.pin_IN1, False)
		GPIO.output(self.configura.pin_IN2, False)
		controle_motor_dir.ChangeDutyCycle(velocidade)

		GPIO.output(self.configura.pin_IN3, False)
		GPIO.output(self.configura.pin_IN4, False)
		controle_motor_esq.ChangeDutyCycle(velocidade)







