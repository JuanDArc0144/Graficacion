# TRANSFORMACIONES GEOMETRICAS EJERCICIO 

```python
import cv2 as cv
import numpy as np
import math
img = cv.imread('imagenes/tuxYRei.jpg',0)
imgo = cv.imread('imagenes/tuxYRei.jpg',0)
x, y = img.shape
scale_x, scale_y = 2,2
x_s = int(x*scale_x)
y_s = int(y*scale_y)
s_img = np.zeros((int(x_s), int(y_s)), dtype=np.uint8)
#Aplicar el escalado
for i in range(0,x):
    for j in range(0,y):
        s_img[i*2, j*2] = img[i,j]
for i in range(0,x_s-1):
    for j in range(0,y_s-1):
        if s_img[i,j] == 0 & i%2!=0:
            s_img[i,j] = int(s_img[i-1,j] + s_img[i+1,j])/9
        if s_img[i,j] == 0 & i%2==0:
            s_img[i,j] = int(s_img[i-1,j+1] + s_img[i+1,j+1] + s_img[i-1,j-1] + s_img[i+1,j-1])/9
        if s_img[i,j] == 0 & j%2==0:
            s_img[i,j] = int(s_img[i-1,j+1] + s_img[i+1,j+1] + s_img[i-1,j-1] + s_img[i+1,j-1])/9
        if s_img[i,j] == 0 & j%2!=0:
            s_img[i,j] = int(s_img[i-1,j+1] + s_img[i+1,j+1] + s_img[i-1,j-1] + s_img[i+1,j-1])
cv.imshow('Original', imgo)
cv.imshow('Escalada', s_img)
cv.waitKey()
cv.destroyAllWindows
```