import RPi.GPIO as GPIO

class Variaveis:

	def __init__(self):
		self.velocidade = 60

		self.pin_pwm_motor_direita = 13
		self.pin_motor_direita_frente = 19
		self.pin_motor_direita_tras = 26

		self.pin_pwm_motor_esquerda = 12
		self.pin_motor_esquerda_frente = 16
		self.pin_motor_esquerda_tras = 20
