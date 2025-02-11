import cv2 as cv
import numpy as np
lienzo = np.ones((1000,1000), dtype=np.uint8) *250
for i in range(1000):
    for j in range(1000):
        if i%25==0 & j%25==0:
            lienzo[i,j]= 1
            lienzo[j,i] = 1
for i in range(175*2+75, 325*2-75):
    for j in range(50, 75):
        lienzo[j, i] = 1
for i in range(175*2+75, 200*2-75):
    for j in range(50, 100):
        lienzo[j, i] = 1
for i in range(150*2+75, 175*2+75):
    for j in range(75, 100):
        lienzo[j, i] = 1
    for j in range(100, 125):
        lienzo[j,i] = 1
for i in range(125*2+75,150*2+75):
    for j in range(125, 150):
        lienzo[j,i] = 1
    for j in range(100, 125):
        lienzo[j,i] = 1
for i in range(100*2+75,125*2+75):
    for j in range(125, 150):
        lienzo[j,i] = 1
    for j in range(150, 175):
        lienzo[j,i] = 1
cv.imshow('LINK', lienzo)
cv.waitKey(0)
cv.destroyAllWindows