#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:44:38 2020

@author: estanislau
"""


import cv2

video = cv2.VideoCapture("video.mp4")

while(True):
    status, frame = video.read()
    
    # Redimensionamento da imagem
    imagem = cv2.resize(frame, (400, 200))
      
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    imagem_blur = cv2.GaussianBlur(imagem_cinza,(5,5),0)
    
    imagem_tresh = cv2.inRange(imagem_blur, 240, 255) 
    
    imagem_canny = cv2.Canny(imagem_blur, 240, 250)
    
    imagem_final = cv2.add(imagem_tresh, imagem_canny)
    
    #cv2.imshow("Imagem Original", imagem)  
    #cv2.imshow("Imagem Cinza", imagem_cinza)
    #cv2.imshow("Imagem Blur", imagem_blur)
    cv2.imshow("Imagem Tresh", imagem_tresh)
    cv2.imshow("Imagem Canny", imagem_canny)
    cv2.imshow("Imagem Final", imagem_final)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows() 