import cv2 as cv
import numpy as np
import random as rm
def generar_punto_elipse(a, b, t):
    x = int(a * 2* np.cos(t) + 750)  # Desplazamiento para centrar
    y = int(b * np.sin(t) + 400)
    return (x, y)
a = 200
b = 150
num_puntos = 500
t_vals = np.linspace(0, 2 * np.pi, num_puntos)
t_vals2 = np.linspace(0, 2*np.pi, num_puntos)
for i in t_vals:
    img = np.ones((800, 1500, 3), dtype=np.uint8)*0
    cv.circle(img, (750, 400), 90, (82,181, 255), -1)
    # cv.circle(img, (750, 250), 45, (0,234, 21), 3)
    # cv.circle(img, (750, 550), 45, (0,234, 21), 3)
    # cv.circle(img, (600, 400), 45, (0,234, 21), 3)
    # cv.circle(img, (900, 400), 45, (0,234, 21), 3)
    aa = a + 100
    bb = b + 75
    aaa = a + 50
    bbb = b + 32
    aaaa = a  + 150
    bbbb = b + 180
    punto4 = generar_punto_elipse(aaaa, bbbb, i)
    punto3 = generar_punto_elipse(aaa,bbb,i)
    punto2 = generar_punto_elipse(aa,bb, i)
    punto = generar_punto_elipse(a,b,i)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse(a, b, t_tray)
        cv.circle(img, pt_tray, radius=1, color=(255,255,255), thickness=-1)
    for t_tray2 in t_vals2:
        pt_tray = generar_punto_elipse(aa, bb, t_tray2)
        cv.circle(img, pt_tray, radius=1, color=(255,255,255), thickness=-1)
    for t_tray2 in t_vals2:
        pt_tray = generar_punto_elipse(aaa, bbb, t_tray2)
        cv.circle(img, pt_tray, radius=1, color=(255,255,255), thickness=-1)
    for t_tray2 in t_vals2:
        pt_tray = generar_punto_elipse(aaaa, bbbb, t_tray2)
        cv.circle(img, pt_tray, radius=1, color=(255,255,255), thickness=-1)
    cv.circle(img, punto, radius=20, color=(0, 0, 255), thickness=-1)
    cv.circle(img, punto2, radius=20, color=(190, 190, 190), thickness=-1)
    cv.circle(img, punto3, radius=20, color=(0, 255, 0), thickness=-1)
    cv.circle(img, punto4, radius=20, color=(255, 0, 0), thickness=-1)
    cv.imshow('animacion', img)
    cv.waitKey(5)
cv.destroyAllWindows