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

import RPi.GPIO as GPIO
from configuracoes import Configuracoes

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

class Main():

	def __init__(self):
		self.configura = Configuracoes()


	def main(self):
		self.configura.pinos_GPIOS()


if __name__ == '__main__':
	execute_app = Main()
	execute_app.main()
