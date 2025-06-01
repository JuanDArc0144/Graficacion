# FILTRO DEL ROSTRO

```python
import cv2 as cv 
rostro = cv.CascadeClassifier('imagenes/haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()
    gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gris, 1.3, 5)
    for(x,y,w,h) in rostros:
        res = int((w+h)/8)
        #img = cv.rectangle(img, (x,y), (x+w, y+h), (234, 23,23), 5)
        #img = cv.rectangle(img, (x,int(y+h/2)), (x+w, y+h), (0,255,0),-1 )
        img = cv.circle(img, (x+int(h/2), y+int(w/2)), int(2*w), (110,110,110), 3)
        img = cv.circle(img, (x+int(h/2), y+int(w/2)), int(w), (110,110,110), 5)
        img = cv.circle(img, (x+int(h/2), y+int(w/2)), int(1.5*w), (110,110,110), 4)
        img = cv.circle(img, (x+int(h/2), y+int(w/2)), int(2.5*w), (110,110,110), 2)
        img = cv.circle(img, (x+int(h/2), y+int(w/2)), int(w/6), (0,0,255), -1)
        img = cv.circle(img, (x+int(h/2), y+int(w/2)), int(w*3), (110,110,110), 1)
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.5)) , 18, (110, 110, 110), -1 )
        img = cv.circle(img, (x + int(w*0.69), y + int(h*0.65)) , 18, (110, 110, 110), -1 )
        img = cv.circle(img, (x + int(w*0.62), y + int(h*0.34)) , 18, (110, 110, 110), -1 )
        img = cv.circle(img, (x + int(w*1.7), y + int(h*1.4)) , 21, (255, 0, 0), -1 )
        img = cv.circle(img, (x + int(w*2.5), y + int(h*0.8)) , 21, (255, 0, 0), -1 )
        #img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 20, (255, 255, 255), -1 )
        #img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 20, (255, 255, 255), -1 )
        #img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 5, (255, 0, 0), -1 )
        #img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 5, (255, 0, 0), -1 )
    cv.imshow('img', img)
    if cv.waitKey(1)== ord('q'):
        break
cap.release
cv.destroyAllWindows()
```