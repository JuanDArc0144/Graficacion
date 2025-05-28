#Realizar una figura en 3D que podamos rotar
import cv2 as cv
import mediapipe as mp
import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluCylinder, gluSphere
mp_manos = mp.solutions.hands
dibujo_m = mp.solutions.drawing_utils
manos = mp_manos.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
cap = cv.VideoCapture(1)
camera_pos = [4.0, 3.0, 8.0]  # Posición de la cámara
camera_target = [0.0, 1.0, 0.0]  # Punto al que mira
camera_up = [0.0, 1.0, 0.0]  # Vector hacia arriba
#HACER FIGURA
def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(120, 1.0, 0.1, 100.0)  # Campo de visión más amplio
    glMatrixMode(GL_MODELVIEW)

#Olvide documentar el proceso de creación que ya olvide que estaba haciendo XD
def figura(bool):
    cabeza(bool)
    cuerpo(bool)
    brazos(bool)
    piernas(bool)
def dibujar(marcas, frame):
    h,w = frame.shape()
    dedos = [(int(marcas.landmark[i].x * w), int(marcas.landmark[i].y * h)) for i in range(21)]
    pulgar, indice, medio, anular, meñique = dedos[4], dedos[8], dedos[12], dedos[16], dedos[20]
    if indice[1] < 135 and indice[0] > 435 and indice[0] < 533:
        figura(0)
    if indice[1] > 220 and indice[0] > 435 and indice[0] < 533:
        figura(1)
    if indice[0] < 445 and indice[1] > 135 and indice[1] < 220:
        figura(2)
    if indice[0] > 528 and indice[1] > 135 and indice[1] < 220:
        figura(3)
while cap.isOpened():   
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.flip(frame, 1)
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = manos.process(rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            dibujar(hand_landmarks, rgb)
    cv.rectangle(frame, (368, 50), (611, 300), (255,0,0), 5) #1
    cv.rectangle(frame, (435, 135), (533, 220), (255,0,0), 5) #2
    cv.line(frame, (445, 50), (445, 300), (255, 0, 0), 5) #Vertical1 (tomar el eje x)
    cv.line(frame, (528, 50), (528, 300), (255, 0, 0), 5) #Vertical2
    cv.line(frame, (368, 135), (611, 135), (255, 0, 0), 5) #Horizontal1 (tomar el eje y)
    cv.line(frame, (368, 220), (611, 220), (255, 0, 0), 5) #Horizontal2
    cv.imshow("TECLAS", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
