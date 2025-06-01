# RASTRO DE MOVIMIENTO 

```python
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
mask2 = np.zeros((480, 640), dtype=np.uint8)
while(True):
    ret, img = cap.read()
    if ret:
        cv.imshow('video', img)
        hsv =  cv.cvtColor(img, cv.COLOR_BGR2HSV)#Para hacer la segmentacion se necesita HSV
        uba = (100, 255, 255) #Para color verde
        ubb = (30, 40 ,40) #Pureza y brillantez en las otras dos variables
        mask = cv.inRange(hsv, ubb, uba)
        res = cv.bitwise_and(img, img, mask=mask)
        x, y = img.shape[:2]
        print(x)
        for i in range(x):
            for j in range(y):
                if mask[i,j] == 255:
                    mask2[i,j] = 255
        cv.imshow('res', res)
        cv.imshow('mask', mask)
        cv.imshow('rastro', mask2)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
    else:
        break
cap.release
cv.destroyAllWindows
```