import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluCylinder, gluSphere
import sys
import mediapipe as mp
import cv2
import threading
import math
import numpy as np
ancho_plano = 5
from pynput.keyboard import Key, Controller
keyboard = Controller()
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
radio = 0
def base():
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glVertex3f(-ancho_plano, 0, ancho_plano)
    glVertex3f(ancho_plano, 0, ancho_plano)
    glVertex3f(ancho_plano, 0, -ancho_plano)
    glVertex3f(-ancho_plano, 0, -ancho_plano)
    glEnd()
#VARIABLES DE LA CAMARA
camera_pos = [4.0, 3.0, 8.0]  # Posición de la cámara
camera_target = [0.0, 1.0, 0.0]  # Punto al que mira
camera_up = [0.0, 1.0, 0.0]  # Vector hacia arriba
# VARIABLES DEL MOVIMIENTO
camera_speed = 0.5 # Velocidad de movimiento
keys = {}  # Diccionario para controlar el estado de las teclas
def brazos(x,y,z,a, q):
     glPushMatrix()
     glColor3f(1,0,1)  
     glTranslatef(x,z,y)
     glRotatef(a,x,z,y)
     quadric = gluNewQuadric()
     if q == 0:
        gluSphere(quadric, 1.5, 32, 32)
     else:
        gluSphere(quadric, 1.75, 32, 32)
     glPopMatrix()
def pies(x,y,z,a):
    glPushMatrix()
    glColor3f(1,0.411764,0.380392)
    glTranslatef(x,z,y)
    glRotatef(a,x,z,y)
    quadric = gluNewQuadric()
    gluSphere(quadric, 1.9, 32,32)
    glPopMatrix()
def dibujar_kirby(x,y,z,a):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],  # Posición de la cámara
              camera_target[0], camera_target[1], camera_target[2],  # Punto al que mira
              camera_up[0], camera_up[1], camera_up[2])
    glPushMatrix()
    glColor3f(1,0,1)
    glTranslatef(x,z,y)
    glRotatef(a,x,z,y)
    quadric = gluNewQuadric()
    gluSphere(quadric, 5, 32, 32)
    glPopMatrix()
    brazos(x+1, y+5, z, a, 0)
    brazos(x+1, y-5, z, a, 1)
    pies(x,y+2,z-4,a)
    pies(x,y-2,z-4,a)
    # reflejos_azules(x,y,z,a)
    # reflejos_blancos(x,y,z,a)
    # mejillas(x,y,z,a)
    # boca(x,y,z,a)
    glfw.swap_buffers(window)
def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.6, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad
    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(120, 1.0, 0.1, 100.0) 
    glMatrixMode(GL_MODELVIEW)
#def movimiento_figura(hand_landmarks, frame):
def key_callback(window, key, scancode, action, mods):
    """Actualiza el estado de las teclas"""
    if action == glfw.PRESS:
        keys[key] = True
    elif action == glfw.RELEASE:
        keys[key] = False
def dibujar_circulo(hand_landmarks, frame):
    global radio
    y, x, z = frame.shape
    puntos = [(int(hand_landmarks.landmark[i].x * x), int(hand_landmarks.landmark[i].y * y)) for i in range(21)]
    pulgar, indice, medio, anular, menique, base_medio = puntos[4], puntos[8], puntos[12], puntos[16], puntos[20], puntos[9]
    distancia_pulgarYBase = np.linalg.norm(np.array(pulgar) - np.array(base_medio))
    distancia_indiceYBase = np.linalg.norm(np.array(indice) - np.array(base_medio))
    distancia_medioYBase = np.linalg.norm(np.array(medio) - np.array(base_medio))
    distancia_anularYBase = np.linalg.norm(np.array(anular) - np.array(base_medio))
    distancia_meniqueyBase = np.linalg.norm(np.array(menique) - np.array(base_medio))
    distancia_pulgarYMedio = np.linalg.norm(np.array(pulgar) - np.array(medio))
    radio = int((distancia_pulgarYBase + distancia_indiceYBase + distancia_medioYBase + distancia_anularYBase + distancia_meniqueyBase)/5)
    # cv2.circle(frame, (base_medio[0], base_medio[1]), radio+12, (0,0,204), 3)
    # cv2.circle(frame, (base_medio[0], base_medio[1]), radio+8, (0,0,204), 3)
def controlador(hand_landmarks, frame):
    global camera_pos
    y, x, z = frame.shape
    puntos = [(int(hand_landmarks.landmark[i].x * x), int(hand_landmarks.landmark[i].y * y)) for i in range(21)]
    pulgar, indice, medio, anular, menique, base_medio = puntos[4], puntos[8], puntos[12], puntos[16], puntos[20], puntos[9]
    arriba_indice, mitad_indice = puntos[7], puntos[6]
    if indice[1] < arriba_indice[1] and indice[1] < mitad_indice[1]:
        if indice[0] > mitad_indice[0]:
            camera_pos[1] += camera_speed
            camera_pos[0] += camera_speed
            print("RIGHT-up")
        elif indice[0] < mitad_indice[0]:
            camera_pos[0] -= camera_speed
            print("LEFT-up")
    elif indice[1] > arriba_indice[1] and indice[1] > mitad_indice[1]:
        camera_pos[1] -= camera_speed
        if indice[0] > mitad_indice[0]:
            camera_pos[1] += camera_speed
            camera_pos[0] += camera_speed
            print("RIGHT-down")
        elif indice[0] < mitad_indice[0]:
            camera_pos[0] -= camera_speed
            print("LEFT-down")
def process_input():
    """Procesa el estado de las teclas para mover la cámara"""
    global camera_pos
    if keys.get(glfw.KEY_W, False):  # Mover hacia adelante
        camera_pos[2] -= camera_speed
    if keys.get(glfw.KEY_S, False):  # Mover hacia atrás
        camera_pos[2] += camera_speed
    if keys.get(glfw.KEY_A, False):  # Mover a la izquierda
        camera_pos[0] -= camera_speed
    if keys.get(glfw.KEY_D, False):  # Mover a la derecha
        camera_pos[0] += camera_speed
cap = cv2.VideoCapture(0)
def main():
    global window 
    global textura_cara
    global radio
    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Mover Escena Completa", None, None)
    if not window:
        glfw.terminate()
        sys.exit()
    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()
    # Configurar callback de teclado
    glfw.set_key_callback(window, key_callback)
    # Bucle principal
    while not glfw.window_should_close(window):
        process_input()  # Procesar teclas presionadas
        base()
        dibujar_kirby(0,0,0,0)
        glfw.poll_events()
    glfw.terminate()
    if __name__ == "__main__":
        main()
#hilo con opengl
opengl_thread = threading.Thread(target=main)
opengl_thread.start()
while cap.isOpened():
    ret, frame = cap.read()
    frame= cv2.flip(frame,1)
    if not ret:
        break
    # Convertir a RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            dibujar_circulo(hand_landmarks, frame)
            controlador(hand_landmarks, frame)
            print(radio)
    cv2.imshow("Modelado 3D", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
