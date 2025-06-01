# EJERCICIO EN CLASE HSV

```python
import cv2 as cv
import numpy as np
#Segmentación de modelo de color en HSV. 
#El espectro HSV se descompone en: 
#H = Indica el grado en el que se encuentra un color principal
img = cv.imread('imagenes/nanbaka.jpg', 1)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
uba_orange=(23, 255, 255)
ubb_orange = (12, 40, 40)
uba_blue=(129, 255, 255)
ubb_blue=(102, 40, 40)
uba_pink = (158, 255, 255)
ubb_pink = (142, 40, 40)
uba_yellow = (72, 255, 255)
ubb_yellow = (54, 20, 20)
uba_red1 = (1, 255, 255)
ubb_red1 = (0, 40, 40)
uba_red2 = (180, 255, 255)
ubb_red2 = (176, 40, 40)
mask_red1 = cv.inRange(hsv, ubb_red1, uba_red1)
mask_red2 = cv.inRange(hsv, ubb_red2, uba_red2)
mask_yellow = cv.inRange(hsv, ubb_yellow, uba_yellow)
mask_pink = cv.inRange(hsv, ubb_pink, uba_pink)
mask_blue = cv.inRange(hsv, ubb_blue, uba_blue)
mask_orange = cv.inRange(hsv, ubb_orange, uba_orange)
maskfr = mask_red1 + mask_red2
res = cv.bitwise_and(img, img, mask=mask_orange)
res2 = cv.bitwise_and(img, img, mask=mask_blue)
res3 = cv.bitwise_and(img, img, mask=mask_pink)
res4 = cv.bitwise_and(img, img, mask=mask_yellow)
res5 = cv.bitwise_and(img, img, mask=maskfr)
cv.imshow('original', img)
cv.imshow('orange', res)
cv.imshow('blue', res2)
cv.imshow('pink', res3)
cv.imshow('yellow',res4)
cv.imshow('red', res5)
cv.waitKey(0)
cv.destroyAllWindows
```