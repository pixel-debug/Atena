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
import numpy as np

# Inicializacao da camera e parâmetros de resolucao e quadros por segundo capturado
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)


largura_imagem, altura_imagem = 400, 400
cont_imagem = 1

# Função para rotacionar imagem 180º
def rotaciona_imagem(img):
	# Armazenamento das dimensoes dos frames e criacao do vetor com referencia aos pixels do centro da imagem
	(h, w) = img.shape[:2]
	centro_imagem = (w / 2, h / 2)

	# Utilizacao da funcao RotationMatrix2D para realizar a rotacao da imagem a partir do ponto central
	M = cv2.getRotationMatrix2D(centro_imagem, 180, 1.0)

	# Realiza a rotacao da imagem a partir das funcoes determinadas acima
	img_rotacionada = cv2.warpAffine(img, M, (w, h))

	return img_rotacionada


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array


	if cv2.waitKey(1) & 0xFF == ord('c'):
		salva_imagem = rotaciona_imagem(imagem)
		salva_imagem = cv2.resize(salva_imagem[y:y + h, x:x + w], (largura_imagem, altura_imagem))
		cv2.imwrite("Imagens/" + str(cont_imagem) + ".jpg",salva_imagem)
		print(str(cont_imagem)+"º imagem capturada com sucesso! Pressione 'ESC' para encerrar...")
		cont_imagem += 1    
	
	imagem_rotacionada = rotaciona_imagem(imagem)
	
	cv2.imshow("Streaming Camera Atena", imagem_rotacionada)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()

