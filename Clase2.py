import cv2 as cv
import numpy as np
img = cv.imread('tuxYRei.jpg', 1)
#Crea una matriz de solo 0's
img2 = np.zeros((img.shape[:2]), dtype=np.uint8) 
img0 = cv.imread('tuxYRei.jpg', 0)
#Divide la imagen en 3 matrices, separando los colores rgb
r, g, b = cv.split(img)
#En lugar de RGB, es BGR (se ordena al revés)
r2 = cv.merge([img2, img2, r])
g2 = cv.merge([img2, g, img2])
b2 = cv.merge([b, img2, img2])
img3 = cv.merge([b,r,g])
img4 = cv.merge([g,r,b])
img5= cv.merge([b, g, r])
img6 = cv.merge([r, b, g])
img7 = cv.merge([g, b, r])
'''
cv.imshow('R', r2)
cv.imshow('G', g2)
cv.imshow('B', b2)
cv.imshow('BRG', img3)
cv.imshow('GRB', img4)
cv.imshow('BGR', img5)
cv.imshow('RBG', img6)
cv.imshow('GBR', img7)
cv.imshow('Original', img)
'''
cv.imshow('B&W', img0)
print(img.shape)
cv.waitKey(0)
cv.destroyAllWindows
