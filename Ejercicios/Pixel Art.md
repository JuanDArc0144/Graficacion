# PIXEL ART (LINK)

```python
import cv2 as cv
import numpy as np
#Creación de la matriz 1000x1000
#Las coordenadas (x,y) aqui son x para up-down y y para left.
Negro = 1
Verde = 100
Amarillo = 165
Link = 187
Blanco = 250
Verde_B = 200
Cafe = 50
img = np.ones((1000,1000), dtype=np.uint8) *250
#En estos ciclos se convierte en una red (cada cuadrito es de 25x25)
for i in range(1000):
    for j in range(1000):
        if i%25==0 & j%25==0:
            img[i,j]= Negro
            img[j,i] = Negro
for i in range(425, 575):
    for j in range(50, 75):
        img[j, i] = Negro
for i in range(425, 450):
    for j in range(75, 100):
        img[j,i] = Negro
        for k in range(450, 550):
            img[j,k] = Verde
        for k in range(550, 600):
            img[j,k] = Negro
for i in range(400, 425):
    for j in range(100, 125):
        img[j,i] = Negro
        for k in range(425, 575):
            img[j,k] = Verde
        for k in range(575, 625):
            img[j,k] = Negro
    for j in range(75, 100):
        img[j,i] = Negro
    for j in range(150, 175):
        img[j,i] = Negro
for i in range(375, 400):
    for j in range(100, 125):
        img[j,i] = Negro
    for j in range(125, 150):
        img[j,i] = Negro
        for k in range(400, 600):
            img[j,k] = Verde
        for k in range(600, 650):
            img[j,k] = Negro
    for j in range(150, 175):
        img[j,i] = Verde
        for k in range(425, 575):
            img[j,k] = Amarillo
        for k in range(575, 600):
            img[j,k] = Negro
        for k in range(600, 625):
            img[j,k] = Verde
        for k in range(625, 650):
            img[j,k] = Negro
    for j in range(175, 200):
        img[j,i] = Negro
        for k in range(400, 600):
            img[j,k] = Amarillo
        for k in range(600, 650):
            img[j,k] = Negro
for i in range(350, 375): #De aqui pasó de left-right-up-down a up-down-left-right
    for j in range(125, 150):
        img[j,i] = Negro
    for j in range(150, 175):
        img[j,i] = Negro
    for j in range(175,200):
        img[j,i] = Negro
    for j in range(200,225):
        img[j,i] = Negro
        for k in range(375, 425):
            img[j,k] = Amarillo
        for k in range(425, 450):
            img[j,k] = Negro
        for k in range(450, 550):
            img[j,k] = Amarillo
        for k in range(550, 575):
            img[j,k] = Negro
        for k in range(575, 625):
            img[j,k] = Amarillo
        for k in range(625, 675):
            img[j,k] = Negro
    for j in range(225,250):
        img[j,i] = Negro
        for k in range(275, 375):
            img[j,k] = Negro
        for k in range(375, 400):
            img[j,k] = Amarillo
        for k in range(400, 425):
            img[j,k] = Negro
        for k in range(425, 525):
            img[j,k] = Amarillo
        for k in range(525, 600):
            img[j,k] = Negro
        for k in range(600, 625):
            img[j,k] = Amarillo
        for k in range(625, 725): #Linea de las orejas
            img[j,k] = Negro 
    for j in range(250,275):
        img[j,i] = Negro
        for k in range(300, 350):
            img[j,k] = Link
        for k in range(275, 300):
            img[j,k] = Negro
        for k in range(375, 400):
            img[j,k] = Negro
        for k in range(400, 500):
            img[j,k] = Amarillo
        for k in range(500, 550):
            img[j,k] = Negro
        for k in range(550, 575):
            img[j,k] = Link
        for k in range(575, 600):
            img[j,k] = Negro
        for k in range(600, 625):
            img[j,k] = Amarillo
        for k in range(625, 650):
            img[j,k] = Negro
        for k in range(650, 700):
            img[j,k] = Link
        for k in range(700, 725):
            img[j,k] = Negro
for i in range(275, 300):
    for j in range(475,500): #Medio
        img[i,j] = Negro
    for j in range(450, 475): #1m
        img[i,j] = Negro
    for j in range(400, 450):
        img[i,j] = Amarillo
    for j in range(300, 400):
        img[i,j] = Negro
    for j in range(500, 525): #2m
        img[i,j] = Negro
    for j in range(525, 575):
        img[i,j] = Link
    for j in range(575, 600):
        img[i,j] = Negro
    for j in range(600, 625):
        img[i,j] = Amarillo
    for j in range(625, 700):
        img[i,j] = Negro
for i in range(300, 325):
    for j in range(475, 500):
        img[i,j] = Negro #Medio
    for j in range(375, 475):
        img[i,j] = Negro
    for j in range(350, 375):
        img[i,j] = Amarillo
    for j in range(325, 350):
        img[i,j] = Negro
    for j in range(500, 525): #2m
        img[i,j] = Link
    for j in range(525, 625):
        img[i,j] = Negro
    for j in range(625, 650):
        img[i,j] = Amarillo
    for j in range(650, 675):
        img[i,j] = Negro
for i in range(325, 350):
    for j in range(475, 500):
        img[i,j] = Link #M
    for j in range(425, 475):
        img[i,j] = Negro
    for j in range(400, 425):
        img[i,j] = Blanco
    for j in range(375, 400):
        img[i,j] = Negro
    for j in range(350, 375):
        img[i,j] = Amarillo
    for j in range(325, 350):
        img[i,j] = Negro
    for j in range(500, 525): #2
        img[i,j] = Link
    for j in range(525, 575):
        img[i,j] = Negro
    for j in range(575, 600):
        img[i,j] = Blanco
    for j in range(600,625):
        img[i,j] = Negro
    for j in range(625, 650):
        img[i,j] = Amarillo
    for j in range(650, 675):
        img[i,j] = Negro
for i in range(350, 375):
    for j in range(475, 500): #M
        img[i,j] = Link
    for j in range(450, 475):
        img[i,j] = Blanco
    for j in range(425, 450):
        img[i,j] = Negro
    for j in range(400, 425):
        img[i,j] = Link
    for j in range(325, 400):
        img[i,j] = Negro
    for j in range(500, 525): #2
        img[i,j] = Link
    for j in range(525, 550):
        img[i,j] = Blanco
    for j in range(550, 575):
        img[i,j] = Negro
    for j in range(575, 600):
        img[i,j] = Link
    for j in range(600, 675):
        img[i,j] = Negro
for i in range(375, 400):
    for j in range(475, 500): #M
        img[i,j] = Link
    for j in range(425, 475):
        img[i,j] = Link
    for j in range(350, 425):
        img[i,j] = Negro
    for j in range(500, 575): #2
        img[i,j] = Link
    for j in range(575, 650):
        img[i,j] = Negro
for i in range(400, 425):
    for j in range(475, 500):
        img[i,j] = Negro #M
    for j in range(375, 475):
        img[i,j] = Negro
    for j in range(500, 625): #2
        img[i,j] = Negro
for i in range(425, 450):
    for j in range(475, 500):
        img[i,j] = Verde #M
    for j in range(425, 475):
        img[i,j] = Verde
    for j in range(400, 425):
        img[i,j] = Negro
    for j in range(375, 400):
        img[i,j] = Verde_B
    for j in range(350, 375):
        img[i,j] = Negro
    for j in range(500, 575): #2
        img[i,j] = Verde
    for j in range(575, 600):
        img[i,j] = Negro
    for j in range(600, 625):
        img[i,j] = Verde_B
    for j in range(625, 650):
        img[i,j] = Negro
for i in range(450, 475):
    for j in range(475, 500):
        img[i,j] = Verde #M
    for j in range(425,475):
        img[i,j] = Verde
    for j in range(400, 425):
        img[i,j] = Negro
    for j in range(350, 400):
        img[i,j] = Verde_B
    for j in range(325, 350):
        img[i,j] = Negro
    for j in range(500, 575): #2
        img[i,j] = Verde
    for j in range(575, 600):
        img[i,j] = Negro
    for j in range(600, 650):
        img[i,j] = Verde_B
    for j in range(650, 675):
        img[i,j] = Negro
for i in range(475, 500):
     for j in range(475, 500):
         img[i,j] = Verde #M
     for j in range(425, 475):
         img[i,j] = Verde
     for j in range(375, 425):
         img[i,j] = Negro
     for j in range(325, 375):
         img[i,j] = Link
     for j in range(300, 325):
        img[i,j] = Negro
     for j in range(500, 575): #2
        img[i,j] = Verde
     for j in range(575, 625):
        img[i,j] = Negro
     for j in range(625, 675):
        img[i,j] = Link
     for j in range(675, 700):
        img[i,j] = Negro
for i in range(500, 525):
    for j in range(475, 500): #M
        img[i,j] = Amarillo
    for j in range(425, 475):
        img[i,j] = Negro
    for j in range(400, 425):
        img[i,j] = Verde
    for j in range(375, 400):
        img[i,j] = Negro
    for j in range(350, 375):
        img[i,j] = Link
    for j in range(300, 350):
        img[i,j] = Negro
    for j in range(500, 525):
        img[i,j] = Amarillo
    for j in range(525, 575):
        img[i,j] = Negro
    for j in range(575, 600):
        img[i,j] = Verde
    for j in range(600, 625):
        img[i,j] = Negro
    for j in range(625, 650):
        img[i,j] = Link
    for j in range(650, 700):
        img[i,j] = Negro
for i in range(525, 550):
    for j in range(475, 500):
        img[i,j] = Amarillo #M
    for j in range(450, 475):
        img[i,j] = Negro
    for j in range(400, 450):
        img[i,j] = Verde
    for j in range(325, 400):
        img[i,j] = Negro
    for j in range(500, 525):
        img[i,j] = Amarillo
    for j in range(525, 550):
        img[i,j] = Negro
    for j in range(550, 600):
        img[i,j] = Verde
    for j in range(600, 675):
        img[i,j] = Negro
for i in range(550, 575):
    for j in range(475, 500):
        img[i,j] = Verde #M
    for j in range(450, 475):
        img[i,j] = Verde
    for j in range(375, 450):
        img[i,j] = Negro
    for j in range(500, 550):
        img[i,j] = Verde
    for j in range(550, 625):
        img[i,j] = Negro
for i in range(575, 600):
    for j in range(475, 500):
        img[i,j] = Negro
    for j in range(450, 475):
        img[i,j] = Negro
    for j in range(375, 450):
        img[i,j] = Cafe
    for j in range(350, 375):
        img[i,j] = Negro
    for j in range(500, 550):
        img[i,j] = Negro
    for j in range(550, 625):
        img[i,j] = Cafe
    for j in range(625, 650):
        img[i,j] = Negro
for i in range(600, 625):
    for j in range(475, 500):
        img[i,j] = Blanco
    for j in range(425, 475):
        img[i,j] = Negro
    for j in range(375, 425):
        img[i,j] = Cafe
    for j in range(350, 375):
        img[i,j] = Negro
    for j in range(500, 525):
        img[i,j] = Blanco
    for j in range(525, 575):
        img[i,j] = Negro
    for j in range(575, 625):
        img[i,j] = Cafe
    for j in range(625, 650):
        img[i,j] = Negro 
for i in range(625, 650):
    for j in range(475, 500):
        img[i,j] = Blanco
    for j in range(450, 475):
        img[i,j] = Blanco
    for j in range(375, 450):
        img[i,j] = Negro
    for j in range(500, 550):
        img[i,j] = Blanco
    for j in range(550, 625):
        img[i,j] = Negro
cv.imshow('LINK' , img)
cv.waitKey(0)
cv.destroyAllWindows
```