import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluCylinder, gluSphere
import sys
ancho_plano = 5
#VARIABLES DE LA CAMARA
camera_pos = [4.0, 3.0, 8.0]  # Posición de la cámara
camera_target = [0.0, 1.0, 0.0]  # Punto al que mira
camera_up = [0.0, 1.0, 0.0]  # Vector hacia arriba


# VARIABLES DEL MOVIMIENTO
camera_speed = 0.01 # Velocidad de movimiento
keys = {}  # Diccionario para controlar el estado de las teclas

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(120, 1.0, 0.1, 100.0)  # Campo de visión más amplio
    glMatrixMode(GL_MODELVIEW)

def base():
    glBegin(GL_QUADS)
    glColor3f(0.3,0.3,0.3)
    glVertex3f(-ancho_plano, 0, ancho_plano)
    glVertex3f(ancho_plano, 0, ancho_plano)
    glVertex3f(ancho_plano, 0, -ancho_plano)
    glVertex3f(-ancho_plano, 0, -ancho_plano)
    glEnd()

def pilar(x):
    cIS = 0.3
    h = 1
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.75)
    glTranslatef(x, 0, 0)
    glRotatef(-90, 1, 0, 0)
    quadric = gluNewQuadric()
    #(quadric, circulo_inferior, circulo_superior, altura)
    gluCylinder(quadric, cIS, cIS, h, 32, 32)
    glPopMatrix()

def reina():
    print()
def figura(x):
    pilar(x)
    if x == 1:
        reina()
    else:
        cuerpo(x)
def dibujar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],  # Posición de la cámara
              camera_target[0], camera_target[1], camera_target[2],  # Punto al que mira
              camera_up[0], camera_up[1], camera_up[2])  # Vector hacia arriba
    base()
    for x in range(3, -3, -1):
        figura(x)
    glfw.swap_buffers(window)
def cuerpo(x):
    cIS = 0.39
    hB = 1
    h = 3
    glPushMatrix()
    glColor3f(0.9, 0.3, 0.75)
    glTranslatef(x, hB, 0)
    glRotatef(-90, 1, 0, 0)
    quadric = gluNewQuadric()
    if x == 2:
        h = 1.5
    else:
        h = 1
    #(quadric, circulo_inferior, circulo_superior, altura)
    gluCylinder(quadric, cIS, cIS, h, 32, 32)
    glPopMatrix()
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
    if keys.get(glfw.KEY_UP, False):  # Subir
        camera_pos[1] += camera_speed
    if keys.get(glfw.KEY_DOWN, False):  # Bajar
        camera_pos[1] -= camera_speed

def key_callback(window, key, scancode, action, mods):
    """Actualiza el estado de las teclas"""
    if action == glfw.PRESS:
        keys[key] = True
    elif action == glfw.RELEASE:
        keys[key] = False

def main():
    global window 
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
        dibujar()
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()


