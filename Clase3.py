import cv2 as cv
import numpy as np
img = cv.imread('tuxYRei.jpg', 1)
#Se puede configurar los modelos de color. 
# Cambia el modelo de color de imagen a un modelo de color en especifico (en este caso, blanco y negro).
img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
img3 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img4 = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img6 = cv.cvtColor(img, cv.COLOR_BGR2XYZ)
img7 = cv.cvtColor(img, cv.COLOR_BGR2Luv)
img8 = cv.cvtColor(img, cv.COLOR_BGR2YUV)
img9 = cv.cvtColor(img, cv.COLOR_BGR2HLS_FULL)
img10 = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
'''
#cv.imshow('Original', img)
# cv.imshow('B&W', img2)
# cv.imshow('RGB', img3)
# cv.imshow('HSV', img4)
# cv.imshow('XYZ', img6)
# cv.imshow('Luv', img7)
# cv.imshow('YUV', img8)
# cv.imshow('HLS', img9)
# cv.imshow('YCR_CB', img10)
#El operador puntual altera el valor del pixel uno por uno, sirve para extraer información y alterar la imagen.
#Este es el operador puntual:
x,y = img.shape[:2]
for i in range(x):
    for j in range(y):
        img2[i,j]=255-img2[i,j]
cv.imshow('pasa', img2)
cv.waitKey(0)
cv.destroyAllWindows