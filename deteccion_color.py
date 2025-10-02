import cv2
import numpy as np

# --- 1. Definir los Rangos de Color (VERDE en HSV) ---
# Los valores HSV van de 0-179 (H), 0-255 (S), 0-255 (V) en OpenCV
# Este rango es para el color VERDE (ajusta si quieres otro color)
verde_bajo = np.array([35, 100, 100])
verde_alto = np.array([85, 255, 255])

# --- 2. Inicializar la Captura de Video ---
cap = cv2.VideoCapture(0)  # 0 para la cámara web principal

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Capturar fotograma por fotograma
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo capturar el fotograma.")
        break

    # --- 3. Convertir a Espacio de Color HSV ---
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # --- 4. Crear la Máscara de Color ---
    # La máscara es una imagen binaria (blanco o negro)
    # donde el blanco son los píxeles dentro del rango definido.
    mask = cv2.inRange(frame_hsv, verde_bajo, verde_alto)

    # --- 5. Aplicar la Máscara al Fotograma Original (Opcional, pero útil) ---
    # Combina la máscara con el fotograma original para mostrar solo el color detectado.
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # --- 6. Mostrar las Ventanas ---
    cv2.imshow('Original', frame)
    cv2.imshow('Mascara (Blanco es el Color Detectado)', mask)
    cv2.imshow('Deteccion de Color', res)

    # Salir del bucle con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- 7. Liberar y Destruir Ventanas ---
cap.release()
cv2.destroyAllWindows()