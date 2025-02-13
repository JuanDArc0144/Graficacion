# Tipo de datos abstractos: Los tipos de datos que define el programador basandose en tipos de datos primitivos.
import cv2 as cv #Se coloca el "as" para reducir el nombre del OpenCV (Convención)
import numpy as np
print(cv.__version__) 
img = np.ones((500,500), dtype=np.uint8) *1
img[30,30] = 255 #Crea un punto blanco en la ubicacion 30,30
img2 = cv.imread('imagenes/tuxYRei.jpg', 1)
img3 = np.zeros((img2.shape[:2]), dtype=np.uint8)
#Separa los valores de la imagen en 3 valores (uno por cada canal de RGB)
r, g, b = cv.split(img2)
img4 = cv.merge([r,g,b])
#np.ones = crea una matriz de puro 1 de 500x500, al multiplicar el 240 se crea una matriz de 240's
#240 = Blanco
#124 = Gris
cv.imshow('img', img4) #img en comillas es el titulo de la ventana
cv.waitKey(0) #mantiene la imagen activa
cv.destroyAllWindows() #permite cerrar la ventana


