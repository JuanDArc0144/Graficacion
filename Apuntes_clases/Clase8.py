#Transformaciones geometricas
#Harrcascades (son modelos entrenados de IA, capaz de detectar rostros, carros, animales, etc.)
import numpy as np
import cv2 as cv
#Permite levantar el archivo xml, utilizando la IA ya entrenada 
rostro = cv.CascadeClassifier('imagenes/haarcascade_frontalface_alt2.xml')
cap = cv.VideoCapture(0)
x=y=w=h= 0 
count = 0
while True:
    ret, frame = cap.read()
    #Una vez leia la imagen, debe pasarse en escala de grises para hacer la deteccion del rostro
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Si existen más de  caracteristicas distinguibles, se detecta como rostro
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    #For para pintar el rectangulo
    for(x, y, w, h) in rostros:
        m= int(h/2)
        #Al pintar el frame, hace el rectangulo en tiempo real. 
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        #frame = cv.rectangle(frame, (x,y+m), (x+w, y+h), (255, 0 ,0), 2 )
        #img = 180- frame[y:y+h,x:x+w]
        #count = count + 1   
    
    #name = '/home/likcos/imgs/cara'+str(count)+'.jpg'
    #cv.imwrite(name, frame)
    cv.imshow('rostros', frame)
    #cv.imshow('cara', img)
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()