#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: HSV

# --------------------------------------------------------


import cv2
import time
import numpy as np
import Variaveis as var






def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)



