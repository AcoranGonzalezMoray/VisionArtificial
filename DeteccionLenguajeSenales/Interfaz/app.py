import tkinter as tk
from tkinter import Label, Button, Scale, Canvas
import cv2
from PIL import Image, ImageTk
import mediapipe as mp
import pyttsx3
import threading
from Mediante_Algoritmo.funciones import clasificadorDePosiciones
from Mediante_Algoritmo.funciones import normalizacionCords

class CameraApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)

        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)
        self.current_letter = ""
        self.detected_letters_str = ""  # String to store detected letters

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

        # Create a frame for buttons
        self.button_frame = tk.Frame(window)
        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=20, anchor='n')

        self.apply_algo = Button(self.button_frame, text="Algoritmo", width=15, command=self.use_algoritmo)
        self.apply_algo.pack(side=tk.TOP, pady=5)

        self.button_snapshot = Button(self.button_frame, text="Read Text", width=15, command=self.read_text)
        self.button_snapshot.pack(side=tk.TOP, pady=5)

        self.apply_yolo = Button(self.button_frame, text="YOLO", width=15, command=self.apply_yolo_algo)
        self.apply_yolo.pack(side=tk.TOP, pady=5)

        self.speed_slider = Scale(self.button_frame, from_=10, to=200, orient=tk.HORIZONTAL, label="Speech Speed", length=200)
        self.speed_slider.set(150)  # Initial speed value
        self.speed_slider.pack(side=tk.TOP, pady=5)

        self.button_reset = Button(self.button_frame, text="Reset Word", width=15, command=self.reset_word)
        self.button_reset.pack(side=tk.TOP, pady=5)

        self.lectura_actual = 0
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.mp_drawing_styles = mp.solutions.drawing_styles

        # Create a canvas for camera feed
        self.canvas = Canvas(window, width=self.vid.get(3), height=self.vid.get(4))
        self.canvas.pack(side=tk.TOP)

        self.label = Label(window, text="Detected Letter: ", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.label_display_letter = Label(window, text="", font=("Helvetica", 16), bd=2, relief="solid", width=50,height=5)
        self.label_display_letter.pack(pady=5)

        self.is_running = True

        # Create a thread for camera capture and processing
        self.camera_thread = threading.Thread(target=self.camera_loop)
        self.camera_thread.start()

        self.detected_letter = None
        self.update()
        self.window.mainloop()

    def camera_loop(self):
        while self.is_running:
            ret, frame = self.vid.read()
            if ret:
                self.use_algoritmo(frame)

    def read_text(self):
        text_to_read = self.label_display_letter.cget("text")  # Get text from the label

        if text_to_read:
            # Run text-to-speech in a separate thread
            threading.Thread(target=self.speak_text, args=(text_to_read,)).start()

    def speak_text(self, text):
        # Set the speech speed before saying the text
        self.engine.setProperty('rate', self.speed_slider.get())
        self.engine.say(text)
        self.engine.runAndWait()

    def reset_word(self):
        self.current_letter = ""
        self.label.config(text="Detected Letter: ")

    def apply_yolo_algo(self):
        return None

    def use_algoritmo(self, frame):
        # Your algorithm implementation goes here
        lectura_actual = 0
        mp_hands = mp.solutions.hands
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape

        # Process the frame with the hand tracking algorithm
        with mp_hands.Hands(
                static_image_mode=False,
                max_num_hands=2,
                min_detection_confidence=0.75) as hands:

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

                # 4 dedos
                for id in range(0, 4):
                    if angulosid[id] > 90:
                        dedos.append(1)
                    else:
                        dedos.append(0)

                dedos, detectedLetter = clasificadorDePosiciones.clasificadorDePosiciones(dedos, frame)

                if detectedLetter:
                    self.label.config(text=f"Detected Letter: {detectedLetter}")

                    # Update detected letters string only if the letter is different
                    if detectedLetter != self.current_letter:
                        self.current_letter = detectedLetter
                        self.detected_letters_str += " " + detectedLetter  # Separate with a space

                        # Update label_display_letter
                        self.label_display_letter.config(text=self.detected_letters_str.strip())

                pinky = normalizacionCords.obtenerAngulos(results, width, height)[1]
                pinkY = pinky[1] + pinky[0]
                resta = pinkY - lectura_actual
                lectura_actual = pinkY
                print(abs(resta), pinkY, lectura_actual)

    def update(self):
        ret, frame = self.vid.read()

        if ret:
            # Convert the OpenCV BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the camera feed on the Tkinter canvas
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

            # Replace the call to main.mainFunction() with self.use_algoritmo()
            self.use_algoritmo(frame)

        # Schedule the update after 10 milliseconds (you can adjust this value)
        self.window.after(10, self.update)

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
