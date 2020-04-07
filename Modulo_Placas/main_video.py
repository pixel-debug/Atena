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

classificadores = [classificador_pare, classificador_pedestre, classificador_desvio]

def detecta_Placas(img_gray, classificador):
    img_placa = classificador.detectMultiScale(img_gray, scaleFactor = 1.1, minNeighbors = 15)
    
    for (x,y,w,h) in img_placa:       
        cv2.rectangle(img_gray, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.putText(img_gray, "Placa", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

    return img_gray

while(True):
    status, frame = video.read()
    
    # Redimensionamento da imagem
    imagem = cv2.resize(frame, (680, 420))
    
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    for i in classificadores:
        imagem_placas = detecta_Placas(imagem_gray, i)
    

    # Apresenta Imagens
    cv2.imshow("Imagem Placas", imagem_placas)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()