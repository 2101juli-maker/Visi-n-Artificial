import cv2
import numpy as np

# --- 1. RANGOS DE COLOR EN HSV (¡CALIBRADOS PARA TUS OBJETOS!) ---

# Rango 1: Color VERDE
# [H Min: 29, S Min: 39, V Min: 25] a [H Max: 95, S Max: 239, V Max: 255]
verde_bajo = np.array([29, 39, 25])
verde_alto = np.array([95, 239, 255])

# Rango 2: Color ROJO (Parte Baja de la Tonalidad, cerca de H=0)
# [H Min: 0, S Min: 164, V Min: 102] a [H Max: 10, S Max: 255, V Max: 255]
rojo_bajo_1 = np.array([0, 164, 102])
rojo_alto_1 = np.array([10, 255, 255]) # Corregido H Max a 10

# Rango 3: Color ROJO (Parte Alta de la Tonalidad, cerca de H=179)
# [H Min: 161, S Min: 7, V Min: 120] a [H Max: 179, S Max: 172, V Max: 207]
rojo_bajo_2 = np.array([161, 7, 120])
rojo_alto_2 = np.array([179, 172, 207])


# --- 2. INICIALIZAR LA CAPTURA DE VIDEO ---
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Capturar fotograma
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo capturar el fotograma.")
        break

    # 3. CONVERTIR A ESPACIO DE COLOR HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 4. CREACIÓN DE MÁSCARAS INDIVIDUALES
    
    # Máscara Verde
    mask_verde = cv2.inRange(frame_hsv, verde_bajo, verde_alto)
    
    # Máscaras de Rojo (Parte 1 y Parte 2)
    mask_rojo_1 = cv2.inRange(frame_hsv, rojo_bajo_1, rojo_alto_1)
    mask_rojo_2 = cv2.inRange(frame_hsv, rojo_bajo_2, rojo_alto_2)
    
    # 5. COMBINAR MÁSCARAS DE ROJO (OR lógico)
    mask_rojo = cv2.bitwise_or(mask_rojo_1, mask_rojo_2)

    # 6. COMBINAR AMBOS COLORES (VERDE y ROJO) en una Máscara Final
    mask_final = cv2.bitwise_or(mask_verde, mask_rojo)
    
    # 7. APLICAR LA MÁSCARA FINAL al fotograma original
    res = cv2.bitwise_and(frame, frame, mask=mask_final)

    # 8. MOSTRAR VENTANAS
    cv2.imshow('Deteccion de VERDE y ROJO', res)
    cv2.imshow('Original', frame)

    # Salir del bucle con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 9. LIBERAR Y DESTRUIR VENTANAS
cap.release()
cv2.destroyAllWindows()