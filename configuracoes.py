#-*- coding utf-8 -*-

# ----------------------- Atena --------------------------

# 	Projeto: Navegação de um robô autônomo educativo 
#            em cenário dinâmico 
# 	Ano: 2020
# 	Orientadora: Natalia Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Configurações

# --------------------------------------------------------
import RPi.GPIO as GPIO

class Configuracoes():
	
	def __init__(self):
		# Motores da Direita
		self.pin_ENA = 12	# PWM motor da direita
		self.pin_IN1 = 20	# Sentido Horário
		self.pin_IN2 = 16	# Sentido Anti-horário

		# Motores da Esquerda
		self.pin_ENB = 13	# PWM motor da esquerda
		self.pin_IN3 = 5		# Sentido Horário
		self.pin_IN4 = 6		# Sentido Anti-horário


	def pinos_GPIOS(self):
		GPIO.setup(self.pin_ENA, GPIO.OUT)
		GPIO.setup(self.pin_IN1, GPIO.OUT)	
		GPIO.setup(self.pin_IN2, GPIO.OUT)
		GPIO.setup(self.pin_ENB, GPIO.OUT)
		GPIO.setup(self.pin_IN3, GPIO.OUT)	
		GPIO.setup(self.pin_IN4, GPIO.OUT)
		print("GPIO's configurados com sucesso...")
