#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:46:04 2020

@author: estanislau
"""


import cv2 
#import glob

image =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Semaforo/211.jpg")
image_c = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = image_c.shape

print(height, width)

nelem = 0
for x in range(210,420):
    for y in range(width):
        if image_c[x,y] < 130:
            nelem += 1
            cv2.floodFill(image, None, (y,x), (0,255,255))

print("Number of elements: ", nelem)

cv2.imshow("image", image)
cv2.waitKey(0)

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