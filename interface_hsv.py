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
camera.resolution = (800, 600)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(800, 600))
time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array

	# Armazenamento das dimensoes dos frames e criacao do vetor com referencia aos pixels do centro da imagem
	(h, w) = imagem.shape[:2]
	centro_imagem = (w / 2, h / 2)

	# Utilizacao da funcao RotationMatrix2D para realizar a rotacao da imagem a partir do ponto central
	M = cv2.getRotationMatrix2D(centro_imagem, 180, 1.0)

	# Realiza a rotacao da imagem a partir das funcoes determinadas acima
	imagem_rotacionada = cv2.warpAffine(imagem, M, (w, h))





