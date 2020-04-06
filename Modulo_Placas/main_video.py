#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:46:04 2020

@author: estanislau
"""


import cv2 
import numpy as np


video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/video.mp4")

classificador_pare = cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_pare.xml')

classificador_pedestre = cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_pedestre.xml')

classificador_desvio = cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_desvio.xml')



while(True):
    status, frame = video.read()
    
    # Redimensionamento da imagem
    imagem = cv2.resize(frame, (680, 420))
    
    imagem_gray = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
			
    imagem_placa_pare = classificador_pare.detectMultiScale(imagem_gray, scaleFactor=1.1, minNeighbors=10)
    
    imagem_placa_pedestre = classificador_pedestre.detectMultiScale(imagem_gray, scaleFactor=1.1, minNeighbors=10)
    
    imagem_placa_desvio = classificador_desvio.detectMultiScale(imagem_gray, scaleFactor=1.1, minNeighbors=10)
	
    for (x,y,w,h) in imagem_placa_pare:
        cv2.rectangle(imagem,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(imagem, "Pare", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
		
    for (x,y,w,h) in imagem_placa_pedestre:
        cv2.rectangle(imagem,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(imagem, "Pedestre", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)    
      
    for (x,y,w,h) in imagem_placa_desvio:
        cv2.rectangle(imagem,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(imagem, "Desvio", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)   
        
    
    # Apresenta Imagens
    cv2.imshow("Imagem", imagem)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()