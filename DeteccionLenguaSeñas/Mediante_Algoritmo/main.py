import cv2
import mediapipe as mp
from Mediante_Algoritmo.funciones.clasificadorDePosiciones import clasificadorDePosiciones
from Mediante_Algoritmo.funciones.normalizacionCords import obtenerAngulos

def main():
    lectura_actual = 0
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    mp_drawing_styles = mp.solutions.drawing_styles

    cap = cv2.VideoCapture(0)

    wCam, hCam = 1280, 720
    cap.set(3, wCam)
    cap.set(4, hCam)

    with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.75) as hands:

        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks is not None:
                angulosid = obtenerAngulos(results, width, height)[0]

                dedos = []
                # pulgar externo angle
                if angulosid[5] > 125:
                    dedos.append(1)
                else:
                    dedos.append(0)

                # pulgar interno
                if angulosid[4] > 150:
                    dedos.append(1)
                else:
                    dedos.append(0)

                # 4 dedos
                for id in range(0, 4):
                    if angulosid[id] > 90:
                        dedos.append(1)
                    else:
                        dedos.append(0)
                #testing--------------------------------------
                print(f'dedos {dedos}')
                #--------------------------------------
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        perfil= False
                        #//////////////////////////////////////////////////////////////////////////////////
                        # Accede a los landmarks tridimensionales
                        landmarks_3d = hand_landmarks.landmark

                        # Obtén las coordenadas x, y, z del primer landmark (puedes ajustar el índice según tus necesidades)
                        x, y, z = landmarks_3d[0].x, landmarks_3d[0].y, landmarks_3d[0].z
                        #x_palma, y_palma, z_palma = landmarks_3d[9].x, landmarks_3d[9].y, landmarks_3d[9].z

                        # Puedes imprimir estas coordenadas para entender mejor la orientación
                        #print(f"Coordenadas del primer landmark: ({x}, {y}, {z})")

                        if z < 3.0e-07:  # Ajusta este umbral según tus necesidades
                            perfil = True
                            print("La mano está de perfil.")
                        else:
                            perfil = False
                            print("La mano no está de perfil.")
                        # //////////////////////////////////////////////////////////////////////////////////
                        clasificadorDePosiciones(dedos, frame, perfil)

                        pinky = obtenerAngulos(results, width, height)[1]
                        pinkY = pinky[1] + pinky[0]
                        resta = pinkY - lectura_actual
                        lectura_actual = pinkY
                        print(abs(resta), pinkY, lectura_actual)

                        if dedos == [0, 0, 1, 0, 0, 0]:
                            if abs(resta) > 30:
                                font = cv2.FONT_HERSHEY_SIMPLEX
                                cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
                                cv2.putText(frame, 'J', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
                        #////////////////////////////////////////////////////////////////////////////////////
                        mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())
            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()