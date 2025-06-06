# Detectar movimiento, utilizando translaciones y transformaciones geométricas. 
# Flujo óptico
# Algoritmos de detección de movimiento a través del cambio de probabilidad de los pixeles. 

```python
import numpy as np
import cv2 as cv
# Iniciar la captura de video desde la cámara
cap = cv.VideoCapture(0)
# Parámetros para el flujo óptico Lucas-Kanade
#Sirven para aumentar el área de flujo y precisión
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# Leer el primer frame de la cámara
#Necesita sacar la diferencia entre valores de pixeles. 
ret, first_frame = cap.read()
prev_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)
ball_pox_aux = np.array([[250, 250]], dtype=np.float32)
# Posición inicial de la pelotita (un único punto en el centro de la imagen)
ball_pos = np.array([[250, 250]], dtype=np.float32)
ball_pos = ball_pos[:, np.newaxis, :]
#El while true se encarga de mantener la cámara prendida
while True:
    # Capturar el siguiente frame
    ret, frame = cap.read()
    if not ret:
        break
    x, y =frame.shape[:2]
    #El flip sirve para quitar el efecto espejo de la cámara
    frame= cv.flip(frame,1)
    # Convertir el frame a escala de grises
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Calcular el flujo óptico para mover la pelotita
    new_ball_pos, st, err = cv.calcOpticalFlowPyrLK(prev_gray, gray_frame, ball_pos, None, **lk_params)
    # Si se detecta el nuevo movimiento, actualizar la posición de la pelotita
    if new_ball_pos is not None:
        ball_pos = new_ball_pos
        # Dibujar la pelotita en su nueva posición
        a, b = ball_pos.ravel()
        if a < 60:
            ball_pos = ball_pox_aux
        if b < 60:
            ball_pos = ball_pox_aux
        if a > (y-60):
            ball_pos = ball_pox_aux
        if b > (x-60):
            ball_pos = ball_pox_aux
        cv.putText(frame, f'{int(a), int(b)}', (int(a-30), int(b-30)), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,25,235), 2)
        frame = cv.circle(frame, (int(a), int(b)), 20, (0, 0, 255), -1)
    else:
        #ARREGLAR POSICION
        ball_pos = ball_pos+1
    cv.rectangle(frame, (60,60), (y-60, x-60), (234,43 ,34) ,5)    
    # Mostrar solo una ventana con la pelotita en movimiento
    cv.imshow('Pelota en movimiento', frame)

    # Actualizar el frame anterior para el siguiente cálculo
    prev_gray = gray_frame.copy()

    # Presionar 'Esc' para salir
    if cv.waitKey(30) & 0xFF == 27:
        break
# Liberar la captura y destruir todas las ventanas
cap.release()
cv.destroyAllWindows()
```