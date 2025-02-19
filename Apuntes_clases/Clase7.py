#Figuras y movimiento de figuras
import cv2 as cv
import numpy as np
#CREAR FIGURAS BASICAS
img = np.ones((500, 500, 3), dtype=np.uint8)*255
cv.circle(img, (250,250), 50, (0,234, 21), -1) #-1 indica que el circulo esta relleno, el 50 indica el radio
#cv.circle(imagen, (posicionx, posiciony), radio, (color), grosor)
cv.line(img, (20,20), (50,60), (0,0,0), 3)
cv.rectangle(img, (20,20), (50,60), (0,0,0), 3)
#MOVER FIGURAS
img2 = np.ones((500,500), dtype=np.uint8)*255
for i in range(400):
    img3 = np.ones(())
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows 
