#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:40:46 2020

@author: estanislau
"""


import cv2
import glob

print("Abrindo pasta Frames_Video/")
for i in sorted(glob.glob('Frames_Video/*.jpg')):  
    #print(i)
    imagem = cv2.imread(i)
    
    cv2.imshow("Apresenta Imagens", imagem)
    cv2.waitKey(1000)

cv2.destroyAllWindows()	