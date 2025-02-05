# Tipo de datos abstractos: Los tipos de datos que define el programador basandose en tipos de datos primitivos.
import cv2 as cv #Se coloca el "as" para reducir el nombre del OpenCV (Convención)
import numpy as np
print(cv.__version__) 
img = np.ones((500,500), dtype=np.uint8) *1
img[30,30] = 255 #Crea un punto blanco en la ubicacion 30,30
for i in range(0,100):
    for j in range(0,100):
        img[i,j] = 255
#np.ones = crea una matriz de puro 1 de 500x500, al multiplicar el 240 se crea una matriz de 240's
#240 = Blanco
#124 = Gris
cv.imshow('img', img) #img en comillas es el titulo de la ventana
cv.waitKey(0) #mantiene la imagen activa
cv.destroyAllWindows() #permite cerrar la ventana


