#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:46:04 2020

@author: estanislau
"""


import cv2 
import numpy as np
#import glob

#imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/248.jpg")
#imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/272.jpg")
#imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/287.jpg")
imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/309.jpg") 


# Imagem da faixa da esquerda
#imagem_obstaculos = imagem_c[210:420, 0:680]

largura, altura = 340, 210

# Redimensionamento da imagem
imagem = cv2.resize(imagem, (largura, altura))
      
imagem_c = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
semente = imagem_c[(altura-1), int(largura/2)]
    
ini_eixo_x = 0
mei_eixo_x = int(largura/2)
fim_eixo_x = largura

ini_eixo_y = (altura-1)
fim_eixo_y = int(altura/2)    

cont_elementos = 0 

for y in range(ini_eixo_y, fim_eixo_y, -1):
    for x in range(mei_eixo_x, fim_eixo_x):
        if imagem_c[y,x] <= 1.7*semente:
            cv2.floodFill(imagem, None, (x, y),(0, 0, 255))
            cont_elementos += 1
        else:
            break
        
    for x in range(mei_eixo_x, ini_eixo_x, -1):
        if imagem_c[y,x]  <= 1.7*semente:
            cv2.floodFill(imagem, None, (x, y),(0, 0, 255))
            cont_elementos += 1
        else:
            break
   
   

    
print(cont_elementos)


# Apresentação Imagens
#cv2.imshow("Imagem Original", imagem)  
cv2.imshow("Imagem Pista", imagem)  
cv2.waitKey(0)    

#if cv2.waitKey(1) & 0xFF == 27:
#break


cv2.destroyAllWindows() 



'''
cont_imagem = 100
for i in sorted(glob.glob('/home/estanislau/Projetos/Atena/Videos/Frames_Semaforo/*.jpg')):  

    imagem = cv2.imread(i)
    
    cv2.imshow("Apresenta Imagem", imagem)
    cv2.waitKey(1000)
    
    print("Frame: {0}".format(cont_imagem))
    cont_imagem += 1
'''  
    
    
    
cv2.destroyAllWindows()