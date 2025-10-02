import cv2
import numpy as np

# --- 1. Funciones de Pista (Trackbars) ---
# Función vacía necesaria para que los deslizadores de OpenCV funcionen.
def nada(x):
    pass

# --- 2. Inicializar la Cámara y Ventana de Calibración ---
cap = cv2.VideoCapture(0)

# El nombre de esta ventana debe coincidir en el punto 3
cv2.namedWindow("Calibracion HSV") 
cv2.resizeWindow("Calibracion HSV", 500, 300) 

# Crear los 6 deslizadores (trackbars) para H, S, V Mínimo y Máximo.
# Se inician con valores típicos para el amarillo (H entre 20 y 35)
# Rango H: 0-179, Rango S y V: 0-255
cv2.createTrackbar("H Min", "Calibracion HSV", 20, 179, nada)
cv2.createTrackbar("S Min", "Calibracion HSV", 100, 255, nada)
cv2.createTrackbar("V Min", "Calibracion HSV", 100, 255, nada)
cv2.createTrackbar("H Max", "Calibracion HSV", 35, 179, nada)
cv2.createTrackbar("S Max", "Calibracion HSV", 255, 255, nada)
cv2.createTrackbar("V Max", "Calibracion HSV", 255, 255, nada)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 3. Convertir a HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 4. Obtener los Valores de los Deslizadores en tiempo real
    h_min = cv2.getTrackbarPos("H Min", "Calibracion HSV")
    s_min = cv2.getTrackbarPos("S Min", "Calibracion HSV")
    v_min = cv2.getTrackbarPos("V Min", "Calibracion HSV")
    h_max = cv2.getTrackbarPos("H Max", "Calibracion HSV")
    s_max = cv2.getTrackbarPos("S Max", "Calibracion HSV")
    v_max = cv2.getTrackbarPos("V Max", "Calibracion HSV")

    # 5. Definir los Rangos con los Valores actuales
    rango_bajo = np.array([h_min, s_min, v_min])
    rango_alto = np.array([h_max, s_max, v_max])

    # 6. Crear la Máscara: Blanco donde el color está dentro del rango
    mask = cv2.inRange(frame_hsv, rango_bajo, rango_alto)
    
    # 7. Aplicar la Máscara para ver solo el color detectado
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 8. Mostrar Resultados
    cv2.imshow('Original', frame)
    cv2.imshow('Deteccion Ajustable', res)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()