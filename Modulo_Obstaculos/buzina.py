import time
import Variaveis as var
import RPi.GPIO as GPIO
import Sensores as sensor
import Configuracoes as definir

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


pin_BUZINA = 22


GPIO.setup(pin_BUZINA, GPIO.OUT)

try:
	while(True):
		GPIO.output(var.pin_BUZINA, True)
		time.sleep(0.2)
		GPIO.output(var.pin_BUZINA, False)
		time.sleep(0.1)
		GPIO.output(var.pin_BUZINA, True)
		time.sleep(0.6)

		GPIO.output(var.pin_BUZINA, False)
		time.sleep(5)
finally:
	print("bye bye...")	
	GPIO.cleanup()
