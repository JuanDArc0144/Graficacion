import cv2 as cv
import numpy as np
import math

#Traslacion
img = cv.imread('imagenes/tuxYRei.jpg.jpg',0) #B&W
imgc = cv.imread('imagenes/nanbaka.jpg', 1)
# x,y = img.shape
# t_img = np.zeros((x,y), dtype=np.uint8)
# #Escalado
scale_x, scale_y = 1.5,1.5
s_img = np.zeros((int(x * scale_x), int(y * scale_y)), dtype=np.uint8)
#Aplicar el escalado
for i in range(x):
    for j in range(y):
        s_img[i*2, j*2] = img[i,j]
# #Rotacion
cv.imshow('Original', imgc)
# cv.imshow('Escalada', s_img)
#El resize de OpenCV tiene banderas que permiten rellenar la imagen en las perdidas
#Convolución (más adelante)
#Escalado sin perdidas (con función de OpenCV)
scale_i = cv.resize(imgc, None, fx=scale_x, fy=scale_y)
cap = cv.VideoCapture(0) #El 0 es porque va a tomar el primer dispositivo conectado a la maquina
while(True):
    ret, imm = cap.read()

cv.imshow('video', imgv)
cv.imshow('Escalada', scale_i)

cv.waitKey(0)
cv.destroyAllWindows