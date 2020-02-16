#-*- coding utf-8 -*-

# ----------------------- Atena --------------------------

# 	Projeto: Navegação de um robô autônomo educativo 
#            em cenário dinâmico 
# 	Ano: 2020
# 	Orientadora: Natalia Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Main

# --------------------------------------------------------

import time
import RPi.GPIO as GPIO
from motores import Motores
from configuracoes import Configuracoes

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


class Main():

	def __init__(self):
		self.configura = Configuracoes()
		self.movimentar = Motores()
		
	def incializacao(self):
		self.configura.pinos_MOTORES()
		self.configura.pinos_VELOCIDADE()
		
	def main(self):
		self.incializacao()

		while(True):	
			self.movimentar.frente(20, self.configura.controle_motor_dir, self.configura.controle_motor_esq)
			time.sleep(1)
			self.movimentar.tras(20, self.configura.controle_motor_dir, self.configura.controle_motor_esq)
			time.sleep(1)

if __name__ == '__main__':
	execute_app = Main()
	execute_app.main()
