import tkinter as tk
from tkinter import Label, Button, Scale, Canvas
import cv2
from PIL import Image, ImageTk
import mediapipe as mp
import pyttsx3
import threading
from ultralytics import YOLO
from Mediante_Algoritmo.funciones import clasificadorDePosiciones
from Mediante_Algoritmo.funciones import normalizacionCords

class CameraApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)

        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)
        self.current_letter = ""
        self.detected_letters_str = ""

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

        self.algo_id = 0
        self.selector_state = tk.BooleanVar()

        # Initialize YOLO for sign language detection
        self.sign_language_model = YOLO('../Mediante_modelo_entrenado/model/best.pt')

        # Create a frame for buttons
        self.button_frame = tk.Frame(window)
        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=20, anchor='n')

        self.change_algorithm = Button(self.button_frame, text="Mediante YOLO", width=15, command=self.change_algorithm)
        self.change_algorithm.pack(side=tk.TOP, pady=5)

        self.button_snapshot = Button(self.button_frame, text="Read Text", width=15, command=self.read_text)
        self.button_snapshot.pack(side=tk.TOP, pady=5)

        label_speed = Label(self.button_frame, text="Speech Speed", font=("Helvetica", 10))
        label_speed.pack(side=tk.TOP, pady=5)

        self.speed_slider = Scale(self.button_frame, from_=10, to=200, orient=tk.HORIZONTAL, length=200)
        self.speed_slider.set(150)
        self.speed_slider.pack(side=tk.TOP, pady=5)

        self.button_reset = Button(self.button_frame, text="Reset TextBox", width=15, command=self.reset_textBox)
        self.button_reset.pack(side=tk.TOP, pady=5)

        self.selector = tk.Checkbutton(self.button_frame, text="On/Off", variable=self.selector_state,
                                       command=self.readCurrentLetter)
        self.selector.pack(side=tk.TOP, pady=5)

        self.lectura_actual = 0
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.mp_drawing_styles = mp.solutions.drawing_styles

        # Create a canvas for the camera feed
        self.canvas = Canvas(window, width=self.vid.get(3), height=self.vid.get(4))
        self.canvas.pack(side=tk.TOP)

        self.label = Label(window, text="Detected Letter: ", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.label_display_letter = Label(window, text="", font=("Helvetica", 16), bd=2, relief="solid", width=50,
                                          height=5, wraplength=300, justify=tk.CENTER)
        self.label_display_letter.pack(pady=5)

        self.sign_language_className = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                                        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                                        "U", "V", "W", "X", "Y", "Z"]

        self.is_running = True
        self.auto_read = False

        # Create a thread for camera capture and processing
        self.camera_thread = threading.Thread(target=self.camera_loop)
        self.camera_thread.start()

        self.detected_letter = None
        self.window.mainloop()

    def camera_loop(self):
        lectura_actual = 0
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        mp_drawing_styles = mp.solutions.drawing_styles

        # Process the frame with the hand tracking algorithm
        with mp_hands.Hands(
                static_image_mode=False,
                max_num_hands=1,
                min_detection_confidence=0.75) as hands:
            while self.is_running:
                ret, frame = self.vid.read()
                if ret:
                    if(self.algo_id == 0):
                        self.window.after(0, self.use_algoritmo, frame, lectura_actual, hands,mp_hands, mp_drawing,mp_drawing_styles )
                    else:
                        self.window.after(1, self.use_yolo_algo, frame, hands, mp_drawing, mp_hands)


    def change_algorithm(self):
        if self.algo_id == 1:
            self.algo_id = 0
            self.change_algorithm.config(text="Mediante YOLO")
        else:
            self.algo_id = 1
            self.change_algorithm.config(text="Mediante Algoritmo")

    def read_text(self):
        text_to_read = self.label_display_letter.cget("text")
        if text_to_read:
            threading.Thread(target=self.speak_text, args=(text_to_read,)).start()

    def readCurrentLetter(self):
        selected_state = self.selector_state.get()
        if selected_state:
            # text_to_read = self.current_letter
            # threading.Thread(target=self.speak_text, args=(text_to_read,)).start()
            self.auto_read = True
            return
        self.auto_read = False
        return

    def speak_text(self, text):
        # Set the speech speed before saying the text
        self.engine.setProperty('rate', self.speed_slider.get())
        self.engine.say(text)
        try:
            self.engine.runAndWait()
        except Exception as e:
            print(f"Speach is busy, hold a second: {e}")

    def reset_textBox(self):
        self.current_letter = ""
        self.detected_letters_str = ""
        self.label_display_letter.config(text="")


    def use_yolo_algo(self, frame, hands, mp_drawing, mp_hands):
        frame = cv2.flip(frame, 1)

        # Detección del esqueleto de la mano con MediaPipe Hands
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result_hands = hands.process(frame_rgb)

        # Perform sign language detection with YOLO
        sign_language_results = self.sign_language_model(frame)

        # Process YOLO results
        for sign_r in sign_language_results:
            boxes = sign_r.boxes
            for box in boxes:
                cls = int(box.cls[0])
                #confidence_threshold = 0.60
                if self.sign_language_className[cls] in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                                                        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                                                        "U", "V", "W", "X", "Y", "Z"]:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    text_width, text_height = cv2.getTextSize(self.sign_language_className[cls], cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]

                    background_width = 150
                    background_height = text_height + 10

                    x1_background = x1
                    y1_background = y2 + 30
                    x2_background = x1_background + background_width
                    y2_background = y1_background - background_height

                    cv2.rectangle(frame, (x1_background, y1_background), (x2_background, y2_background), (255, 255, 255), -1)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    class_name = self.sign_language_className[cls]
                    cv2.putText(frame, "Letter: " + class_name, (x1_background + 10, y1_background - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

                    if class_name:
                        self.label.config(text=f"Detected Letter: {class_name}")

                        if (self.auto_read):
                            threading.Thread(target=self.speak_text, args=(class_name,)).start()

                        elif class_name != self.current_letter:
                            self.current_letter = class_name
                            self.detected_letters_str += " " + class_name  # Separate with a space

                            # Update label_display_letter
                            self.label_display_letter.config(text=self.detected_letters_str.strip())
            # Mostrar el esqueleto de la mano
            if result_hands.multi_hand_landmarks:
                for hand_landmarks in result_hands.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def use_algoritmo(self, frame, lectura_actual,hands, mp_hands,mp_drawing, mp_drawing_styles):
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape
        results = hands.process(frame)

        if results.multi_hand_landmarks is not None:
            angulosid = normalizacionCords.obtenerAngulos(results, width, height)[0]
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

            for id in range(0, 4):
                if angulosid[id] > 90:
                    dedos.append(1)
                else:
                    dedos.append(0)

            for hand_landmarks in results.multi_hand_landmarks:
                perfil = False
                # //////////////////////////////////////////////////////////////////////////////////s
                landmarks_3d = hand_landmarks.landmark
                x, y, z = landmarks_3d[0].x, landmarks_3d[0].y, landmarks_3d[0].z

                if z < 3.0e-07:
                    perfil = True
                    print("La mano está de perfil.")
                else:
                    perfil = False
                    print("La mano no está de perfil.")
                # //////////////////////////////////////////////////////////////////////////////////s
                dedos, detectedLetter = clasificadorDePosiciones.clasificadorDePosiciones(dedos, frame,perfil)

                if detectedLetter:
                    self.label.config(text=f"Detected Letter: {detectedLetter}")

                    if (self.auto_read):
                        threading.Thread(target=self.speak_text, args=(detectedLetter,)).start()

                    # Update detected letters string only if the letter is different
                    elif detectedLetter != self.current_letter:
                        self.current_letter = detectedLetter
                        self.detected_letters_str += " " + detectedLetter  # Separate with a space

                        # Update label_display_letter
                        self.label_display_letter.config(text=self.detected_letters_str.strip())

                pinky = normalizacionCords.obtenerAngulos(results, width, height)[1]
                pinkY = pinky[1] + pinky[0]
                resta = pinkY - lectura_actual
                lectura_actual = pinkY
                print(abs(resta), pinkY, lectura_actual)

                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        # Display the updated frame on the Tkinter canvas
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def __del__(self):
        self.is_running = False  # Stop the camera thread
        self.camera_thread.join()  # Wait for the camera thread to finish
        if self.vid.isOpened():
            self.vid.release()
        cv2.destroyAllWindows()

# Set your camera source (use 0 for default camera)
video_source = 0

root = tk.Tk()
app = CameraApp(root, "Camera App", video_source)
