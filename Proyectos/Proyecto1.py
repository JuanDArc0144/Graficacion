import cv2
import mediapipe as mp
import numpy as np
import random as r
#NOTA IMPORTANTE-------------------------------------------------------------
#PARA DESARROLLAR Z PONER UNOS PEQUEÑOS CIRCULOS QUE SIRVAN DE REFERENCIA AL DEDO. 
#PONER UN TEMPORIZADOR QUE SE IMPRIMA EN CONSOLA PARA VERIFICAR EL TIEMPO QUE TARDA EL USUARIO ES REGISTRAR LA LETRA. 
#POR EJEMPLO, QUE CADA 500 ITERACIONES SE REINICIE EL CONTADOR, Y SI ES MENOR QUE LO REGISTRE COMO VALIDO, LUEGO AL SIGUIENTE CIRCULO
# REGISTRAR SI ES MENOR A 500 DE NUEVO Y ASI HASTA QUE AL FINAL TOME TODAS LAS VALIDACIONES Y QUE MUESTRE LA LETRA Z POR 5 SEGUNDOS. 
#PARA LOS NÚMEROS CREAR UNA FUNCION QUE REGISTRE EL CONTACTO DE LOS DEDOS, VERIFICANDO A TRAVÉS DE TIEMPOS DE RESPUESTA, 
# Y DESPUES REGISTRAR SI EL DEDO INDICE ES MAYOR QUE EL PUNTO MEDIO DEL DEDO MEDIO ESTANDO INCLINADO (NÚMERO 31).
#PARA FAMILIA, SOLO REGISTRAR LA POSICIÓN DE LAS MANOS, NO REGISTRAR BRAZOS, IDENTIFICAR AMBAS MANOS. 
# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
conteo = 0
contador34 = 0
contador51 = 0
frente_v = False
reverso_v = False 
# Función para determinar la letra según la posición de los dedos
def reconocer_letra(hand_landmarks, frame):
    global conteo
    global contador34
    global contador51
    global frente_v
    global reverso_v
    h, w, _ = frame.shape  # Tamaño de la imagen
    # Obtener coordenadas de los puntos clave en píxeles
    dedos = [(int(hand_landmarks.landmark[i].x * w), int(hand_landmarks.landmark[i].y * h)) for i in range(21)]
    # Obtener posiciones clave (puntas de los dedos)
    pulgar, indice, medio, anular, meñique, base_medio = dedos[4], dedos[8], dedos[12], dedos[16], dedos[20], dedos[9]
    medio_pulgar = dedos[3]
    base_medio = dedos[9]
    #PARA CIRCULO
    pp, ip, mp, ap, mep = dedos[4], dedos[8], dedos[12], dedos[16], dedos[20]
    # Mostrar los números de los landmarks en la imagen
    for i, (x, y) in enumerate(dedos):
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)  # Puntos verdes
        cv2.putText(frame, str(i), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
    # Dibujar coordenadas del pulgar
    cv2.putText(frame, f'({int(pulgar[0])}, {int(pulgar[1])})', (pulgar[0], pulgar[1] - 15), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (23, 0, 0), 2, cv2.LINE_AA)
    # Calcular distancias en píxeles
    d_pulgar_indice = np.linalg.norm(np.array(pulgar) - np.array(indice))
    d_indice_medio = np.linalg.norm(np.array(indice) - np.array(medio))
    d_medio_anular = np.linalg.norm(np.array(anular) - np.array(medio))
    d_anular_meñique = np.linalg.norm(np.array(anular) - np.array(meñique))
    # Lógica para reconocer algunas letras
    if d_pulgar_indice < 30 and d_indice_medio < 30 and d_medio_anular < 30 and d_anular_meñique < 30:
        frente_v = False
        reverso_v = False
        contador34 = 0
        conteo = 0
        return "O"  # Seña de la letra A (puño cerrado con pulgar al lado)
    elif ip[1] > pp[1] and mp[1] > pp[1] and ap[1] > pp[1] and ip[1] > mep[1] and mp[1] > mep[1] and ap[1] > mep[1]:
        frente_v = False
        reverso_v = False
        contador34 = 0
        conteo = 0
        return "Y"
    elif pp[1] < ip[1] and pp[1] < mp[1] and ap[1] > pp[1] and ip[1] > pp[1] and pp[1] < medio_pulgar[1]:
        frente_v = False
        reverso_v = False
        contador34 = 0
        conteo = 0
        return "H"
    elif  pp[1] < ip[1] and pp[1] < mp[1] and ap[1] > pp[1] and ip[1] > pp[1] and pp[1] > medio_pulgar[1]:
        frente_v = False
        reverso_v = False
        contador34 = 0
        conteo = 0
        return "21"
    elif ap[1] > mp[1] and ap[1] > ip[1] and mep[1] > mp[1] and mep[1] > ip[1] and pp[1] < ap[1] and pp[1] < mep[1] and mp[1] < ip[1]:
        frente_v = False
        reverso_v = False
        contador34 = 30
        conteo = conteo + 1
        print(conteo)
    elif mp[1] < ip[1] and mp[1] < ap[1] and ap[1] < mep[1] and contador34 == 30 and pp[0] > base_medio[0] and pp[1] > base_medio[1]:
        frente_v = False
        reverso_v = False
        conteo = 0
        return "34"
    elif pp[0] < ip[0] and ip[0] < mp[0] and mp[0] < ap[0] and ap[0] < mep[0] and contador34 != 30:
        frente_v = True
        print("FRENTE TRUE")
    elif pp[0] > ip[0] and ip[0] > mp[0] and mp[0] > ap[0] and ap[0] > mep[0] and contador34 != 30:
        reverso_v = True
        print("REVERSO TRUE")
    elif frente_v == True and reverso_v== True and ip[1] < mp[1] and ip[1] < ap[1] and ip[1] < mep[1]:
        return "51"
    return "Desconocido"
# Captura de video en tiempo real
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame= cv2.flip(frame,1)
    if not ret:
        break
    # Convertir a RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar la imagen con MediaPipe
    results = hands.process(frame_rgb)
    # Dibujar puntos de la mano y reconocer letras
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Identificar la letra
            letra_detectada = reconocer_letra(hand_landmarks, frame)
            # Mostrar la letra en pantalla
            cv2.putText(frame, f"Letra: {letra_detectada}", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    # Mostrar el video
    cv2.imshow("Abecedario", frame)
    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar recursos
cap.release()
cv2.destroyAllWindows()