#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:46:04 2020

@author: estanislau
"""


import cv2 
import glob
import numpy as np




cont_imagem = 100
for i in sorted(glob.glob('/home/estanislau/Projetos/Atena/Videos/Frames_Semaforo/*.jpg')):  

    imagem = cv2.imread(i)
    
    cv2.imshow("Apresenta Imagem", imagem)
    cv2.waitKey(1000)
    
    print("Frame: {0}".format(cont_imagem))
    cont_imagem += 1
    
    
    
    
cv2.destroyAllWindows()