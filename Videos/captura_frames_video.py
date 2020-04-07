#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:22:38 2020

@author: estanislau
"""


import cv2
import time

video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/video.mp4")

cont_imagem = 100
cont_execucao = 1


while(True):
    
    verif, frame = video.read()
    
    imagem = cv2.resize(frame, (680, 420))
    
    if cont_execucao % 10 == 0:
        cv2.imwrite("Frames_Video/" + str(cont_imagem) + ".jpg",imagem)
        print(str(cont_imagem)+"º imagem capturada com sucesso...")
        cont_imagem += 1
    cont_execucao += 1    
	
	
    cv2.imshow("Streaming Camera Atena", imagem)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()