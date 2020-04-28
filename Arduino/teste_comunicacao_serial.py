import serial 

comunicacao = serial.Serial('/dev/ttyUSB0', 9600)

while(True):
	print(comunicacao.readline())
