# PING PONG REALIZADO EN CLASE

```python
import cv2 as cv
import numpy as np
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
    r = 20
    R = R + 30
    G = G + 20
    B = B + 40
    img = np.ones((500, 500, 3), dtype=np.uint8)*255
    cv.circle(img, (x, y), r, (B,G,R), -1)
    if x ==500:
        dx = -dx
        r = r + 150
    if x==0:
        dx = -dx
        r = r + 150
    if y == 500:
        dy = -dy
        r = r + 150
    if y == 0:
        dy = -dy
        r = r + 150
    if R>=255:
        R = 0
    if G>= 255:
        G = 0
    if B >= 255:
        B = 0
    cv.imshow('imagen', img)
    cv.waitKey(40)
cv.destroyAllWindows
```


    


