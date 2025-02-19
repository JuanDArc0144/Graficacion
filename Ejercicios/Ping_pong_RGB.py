import cv2 as cv
import numpy as np
img = np.ones((500, 500, 3), dtype=np.uint8)*255
dx = 5
dy = 5
x = 50
y = 200
R = 0
G = 0
B = 0
for i in range(400):
    x += dx
    y += dy
    R = R + 30
    G = G + 20
    B = B + 40
    img = np.ones((500, 500, 3), dtype=np.uint8)*255
    cv.circle(img, (x, y), 55, (B,G,R), -1)
    if x ==500:
        dx = -dx
    if x==0:
        dx = -dx
    if y == 500:
        dy = -dy
    if y == 0:
        dy = -dy
    if R>=255:
        R = 0
    if G>= 255:
        G = 0
    if B >= 255:
        B = 0
    cv.imshow('imagen', img)
    cv.waitKey(40)
cv.destroyAllWindows

    


