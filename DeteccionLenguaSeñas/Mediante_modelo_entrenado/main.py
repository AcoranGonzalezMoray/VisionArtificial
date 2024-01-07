import cv2
import mediapipe as mp
from ultralytics import YOLO

def main():
    # Inicializar YOLO para la detección de lenguaje de señas
    sign_language_model = YOLO('model/best.pt')

    # Inicializar MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # Inicializar el módulo para dibujar landmarks
    mp_drawing = mp.solutions.drawing_utils

    # Nombre de la clase de interés (puedes ajustar según las clases de tu modelo)
    sign_language_className = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                               "U", "V", "W", "X", "Y", "Z"]

    # Inicializar la cámara (0 para la cámara predeterminada)
    cap = cv2.VideoCapture(0)

    while True:
        # Capturar un solo fotograma
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        # Realizar la detección de lenguaje de señas en el fotograma con YOLO
        sign_language_results = sign_language_model(frame)

        # Detección del esqueleto de la mano con MediaPipe Hands
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result_hands = hands.process(frame_rgb)

        # Para cada detección de lenguaje de señas
        for sign_r in sign_language_results:
            boxes = sign_r.boxes

            for box in boxes:
                cls = int(box.cls[0])

                # Filtrar para mostrar solo las letras del abecedario
                if sign_language_className[cls] in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                                                    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                                                    "U", "V", "W", "X", "Y", "Z"]:
                    # Obtener datos de la detección
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # convertir a enteros

                    # Agregar un fondo blanco alrededor del texto
                    text_width, text_height = \
                    cv2.getTextSize(sign_language_className[cls], cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[
                        0]

                    # Ajustar el tamaño del fondo blanco al texto
                    background_width = 150  # Ajusta según tu preferencia, asegurándote de que sea igual o mayor que el texto
                    background_height = text_height + 10  # Ajusta según tu preferencia

                    # Calcular las coordenadas de las esquinas del fondo blanco
                    x1_background = x1
                    y1_background = y2 + 30
                    x2_background = x1_background + background_width
                    y2_background = y1_background - background_height

                    # Dibujar el fondo blanco
                    cv2.rectangle(frame, (x1_background, y1_background), (x2_background, y2_background),
                                  (255, 255, 255),
                                  -1)

                    # Mostrar la caja delimitadora de la letra
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

                    # Dibujar el nombre de la clase debajo de la caja delimitadora
                    class_name = sign_language_className[cls]
                    cv2.putText(frame, "Letter: " + class_name, (x1_background + 10, y1_background - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)  # Texto negro
        # Mostrar el esqueleto de la mano
        if result_hands.multi_hand_landmarks:
            for hand_landmarks in result_hands.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Mostrar el fotograma con las detecciones en tiempo real
        cv2.imshow('Sign Language Detection', frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
