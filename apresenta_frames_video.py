#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:40:46 2020

@author: estanislau
"""


import cv2
import glob

cont_imagem = 1
vetor = []

import re
'''
b = "A1B2C3"
b = re.sub('[^0-9]', '', b)

# 123
print(b)
'''

print("Abrindo pasta Frames_Video/")
for i in glob.glob('Frames_Video/*.jpg'):
    i = int(re.sub('[^0-9]', '', i))    
    print(i)
    #imagem = cv2.imread(i)
    
    vetor.append(i)
	#cv2.imshow("Apresenta Imagens", imagem)
	#cv2.waitKey(1000)
vetor.sort()
cv2.destroyAllWindows()	