#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:46:04 2020

@author: estanislau
"""


import cv2 
import numpy as np
#import glob

imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/237.jpg")

   
# Imagem da faixa da esquerda
#imagem_obstaculos = imagem_c[210:420, 0:680]


# Redimensionamento da imagem
imagem = cv2.resize(imagem, (680, 420))
      
imagem_c = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    
#th, imagem_th = cv2.threshold(imagem_pista, 220, 255, cv2.THRESH_BINARY);
    
cont_elementos = 0 
###
for y in range(419, 230, -1):
    for x in range(340, 680):
        if imagem_c[y,x] <= 125:
            cv2.floodFill(imagem, None, (x, y),(0, 0, 255))
            cont_elementos += 1
        else:
            break
        
    for x in range(340, 0, -1):
        if imagem_c[y,x] <= 125:
            cv2.floodFill(imagem, None, (x, y),(0, 0, 255))
            cont_elementos += 1
        else:
            break
        
print(cont_elementos)
'''
if imagem_c[x, 680-1] > 125:
        cv2.floodFill(imagem, None, (340, x),255)

for y in range(680):
    if imagem_c[0,y] <= 125:
        cv2.floodFill(imagem, None, (y,0),0)
    if imagem_c[420-1, y] > 125:
        cv2.floodFill(imagem, None, (y, 420-1), 0)
'''
####



# Apresentação Imagens
#cv2.imshow("Imagem Original", imagem)  
cv2.imshow("Imagem Pista", imagem)  
cv2.waitKey(0)    

#if cv2.waitKey(1) & 0xFF == 27:
#break


cv2.destroyAllWindows() 












semente = (420,340)
'''
nelem = 0
for y in range(420):
    for x in range(680):
        if image_c[y,x] < 130:
            nelem += 1
            cv2.floodFill(image, None, (x,y), (0,0,255))

print("Number of elements: ", nelem)
'''

#cv2.imshow("image", image)
#cv2.waitKey(0)






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