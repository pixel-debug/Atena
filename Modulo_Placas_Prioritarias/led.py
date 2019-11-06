import time
import Variaveis as var
import RPi.GPIO as GPIO
import Sensores as sensor
import Configuracoes as definir
import Gerenciador as gerencia

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

try:
	while(True):

		#gerencia.desliga_luzes()

		#gerencia.seta_para_direita()	
		gerencia.luz_de_freio()








finally:
	print("bye bye...")	
	GPIO.cleanup()

pin_SETA_TRAS_ESQ 
