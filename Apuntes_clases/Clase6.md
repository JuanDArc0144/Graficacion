# SEGMENTACIÓN POR COLOR en video

```python
import cv2 as cv

cap = cv.VideoCapture(0) #Puede ser 0 y la cadena de una camara IP (tambien un video)
while(True):
    ret, img = cap.read()
    if ret:
        cv.imshow('video', img)
        hsv =  cv.cvtColor(img, cv.COLOR_BGR2HSV)#Para hacer la segmentacion se necesita HSV
        uba = (90, 255, 255) #Para color verde
        ubb = (30, 40 ,40) #Pureza y brillantez en las otras dos variables
        mask = cv.inRange(hsv, ubb, uba)
        res = cv.bitwise_and(img, img, mask=mask)
        cv.imshow('res', res)
        cv.imshow('mask', mask)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
    else:
        break
cap.release
cv.destroyAllWindows
```



