#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Interface HSV

# --------------------------------------------------------

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# Inicializacao da camera e parâmetros de resolucao e quadros por segundo capturado
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

def nada(x): pass

# -------------------------- Interface HSV ------------------------------------
cv2.namedWindow("Interface_HSV")

cv2.createTrackbar("Valor Minimo - H", "Interface_HSV", 0, 179, nada) #Hue
cv2.createTrackbar("Valor Minimo - S", "Interface_HSV", 0, 255, nada) #Saturation
cv2.createTrackbar("Valor Minimo - V", "Interface_HSV", 0, 255, nada) #Value

cv2.createTrackbar("Valor Maximo - H", "Interface_HSV", 179, 179, nada) #Hue
cv2.createTrackbar("Valor Maximo - S", "Interface_HSV", 255, 255, nada) #Saturation
cv2.createTrackbar("Valor Maximo - V", "Interface_HSV", 255, 255, nada) #Value
# -----------------------------------------------------------------------------


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array

	# Conversao da imagem para HSV
	imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

	# Armazenamento das dimensoes dos frames e criacao do vetor com referencia aos pixels do centro da imagem
	(h, w) = imagem.shape[:2]
	centro_imagem = (w / 2, h / 2)

	# Utilizacao da funcao RotationMatrix2D para realizar a rotacao da imagem a partir do ponto central
	M = cv2.getRotationMatrix2D(centro_imagem, 180, 1.0)

	# Realiza a rotacao da imagem a partir das funcoes determinadas acima
	imagem_rotacionada = cv2.warpAffine(imagem, M, (w, h))

	# Apresentacao dos frames em tempo real
	cv2.imshow("Streaming Camera Atena", imagem_rotacionada)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Metodo para abortar execucao
	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()



