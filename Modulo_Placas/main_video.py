#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:46:04 2020

@author: estanislau
"""


import cv2 
import numpy as np


video = cv2.VideoCapture("video.mp4")


while(True):
    status, frame = video.read()
    
    # Redimensionamento da imagem
    imagem = cv2.resize(frame, (680, 420))
    
    cv2.imshow("Imagem", imagem)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()