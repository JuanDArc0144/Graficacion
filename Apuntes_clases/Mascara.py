import cv2
import mediapipe as mp

# Inicializar MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
# Inicializar dibujador de MediaPipe
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=3, color=(0, 255, 0))  # Puntos verdes
#Creamos una def para reconocer el movimiento de los puntos de ínteres. 
def reconocer_movimiento(face_marks, frame):
    h, w = frame.shape
    #Obtenemos las coordenadas de los puntos clave
    puntos = [(int(face_marks.landmark[i].x * w), int(face_marks.landmarks[i].y * h)) for i in range(478)]
    #mitad_labio_inferior, mitad_labio_superior, orilla_labio_izquierdo, orilla_labio_derecho
    mli, mls, oli, old = puntos[14], puntos[13], puntos[78], puntos[36]
# Captura de video
cap = cv2.VideoCapture(2)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)  # Espejo para mayor naturalidad
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION, mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1))
            
            
    cv2.imshow("Puntos Faciales - MediaPipe", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


