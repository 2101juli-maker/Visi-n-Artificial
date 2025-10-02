import cv2
import numpy as np

# --- 1. RANGO DE COLOR AMARILLO (¡CALIBRADO!) ---
# [H Min: 20, S Min: 100, V Min: 100] a [H Max: 35, S Max: 255, V Max: 255]
amarillo_bajo = np.array([20, 100, 100])
amarillo_alto = np.array([35, 255, 255])


# --- 2. INICIALIZAR LA CÁMARA ---
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3. CONVERTIR A HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 4. CREAR LA MÁSCARA
    # El blanco son los píxeles dentro del rango amarillo
    mask = cv2.inRange(frame_hsv, amarillo_bajo, amarillo_alto)

    # 5. APLICAR LA MÁSCARA
    # Muestra solo el color amarillo
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 6. MOSTRAR VENTANAS
    cv2.imshow('Deteccion de AMARILLO', res)
    cv2.imshow('Original', frame)

    # Salir del bucle con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
