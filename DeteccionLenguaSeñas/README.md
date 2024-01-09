# Proyecto Final | Detección del Lenguaje de Señas
En este proyecto, hemos desarrollado la detección del lenguaje de señas de dos maneras diferentes.

- La primera se realiza de forma manual y se encuentra en el directorio **Mediante_Algoritmo**.
- La segunda se realiza mediante inteligencia artificial utilizando **YOLO**, una biblioteca de detección de objetos, lo cual está localizado en el directorio **Mediante_modelo_entrenado**.

Finalmente, hemos implementado una interfaz que integra ambas metodologías.

## Mediante Algortimo

### Clasificador de Posiciones y Obtención de Ángulos

Este bloque de código en Python utiliza la biblioteca OpenCV (cv2), Mediapipe, y NumPy para implementar un clasificador de posiciones basado en la detección de manos. Además, se obtienen ángulos a partir de las posiciones de los dedos en la mano.

### Clasificador de Posiciones

La función `clasificadorDePosiciones` toma como entrada una lista de dedos (`dedos`), un marco de imagen (`frame`), y un indicador de perfil (`perfil`). Dependiendo de la configuración de los dedos, se identifica una letra correspondiente al lenguaje de señas y se superpone en un rectángulo blanco en la esquina superior izquierda del marco.

### Obtención de Ángulos

La función `obtenerAngulos` utiliza la biblioteca Mediapipe para detectar landmarks en la mano y calcular ángulos basados en las posiciones de los dedos. Los ángulos se calculan en las articulaciones de los dedos y se devuelven como una lista.

#### Coordenadas utilizadas para el cálculo de ángulos:

- Meñique: TIP, PIP, MCP
- Anular: TIP, PIP, MCP
- Medio: TIP, PIP, MCP
- Índice: TIP, PIP, MCP
- Pulgar (parte externa): TIP, IP, MCP
- Pulgar (parte interna): TIP, MCP
- Muñeca: WRIST

La función devuelve una lista de ángulos y las coordenadas del extremo del meñique.

```python
dedos, detected_letter = clasificadorDePosiciones(dedos, frame, perfil)
angulosid, pinky = obtenerAngulos(results, width, height)
```

### Integración de Clasificación de Posiciones y Ángulos
En el código final, se integran el clasificador de posiciones y la obtención de ángulos para lograr una interfaz más completa. La función clasificadorDePosiciones devuelve la letra correspondiente al lenguaje de señas detectada, mientras que obtenerAngulos proporciona información detallada sobre los ángulos formados por las articulaciones de los dedos.

```python
dedos, detected_letter = clasificadorDePosiciones(dedos, frame, perfil)
angulosid, pinky = obtenerAngulos(results, width, height)
```

## Mediante Algoritmo Entrenado
En esta parte, se puede encontrar todo que está relacionado con el entrenamiento del modelo YOLO que hemos utilizado
## Inicialización de Modelos y Librerías

Se utilizan las siguientes bibliotecas y modelos:

- OpenCV para el procesamiento de imágenes.
- MediaPipe Hands para la detección del esqueleto de la mano.
- YOLO (Ultralytics) para la detección de lenguaje de señas.

```python
import cv2
import mediapipe as mp
from ultralytics import YOLO
```
Este script (main.py) proporciona una implementación básica para la detección simultánea de lenguaje de señas y esqueleto de la mano en tiempo real. Puedes ajustar y expandir según tus necesidades específicas.

# Aplicación de Cámara con Interfaz Gráfica

Este script en Python utiliza la biblioteca Tkinter para crear una aplicación de cámara con interfaz gráfica. La aplicación captura un flujo de video de la cámara, realiza la detección de lenguaje de señas mediante el modelo YOLO o un algoritmo personalizado, y proporciona funcionalidades adicionales como la lectura de texto y ajustes de velocidad de habla.

## Clase `CameraApp`

La clase `CameraApp` incluye métodos para inicializar la aplicación y configurar la interfaz, así como funciones para manejar eventos como cambiar entre algoritmos, leer texto y mostrar la detección en tiempo real. Se utiliza threading para ejecutar el bucle de la cámara en segundo plano y garantizar un rendimiento suave de la interfaz.

### Métodos Principales

- `__init__(self, window, window_title, video_source=0)`: Inicializa la aplicación y la interfaz.
- `camera_loop(self)`: Bucle principal para capturar y procesar los fotogramas de la cámara.
- `change_algorithm(self)`: Cambia entre los algoritmos de detección (YOLO o personalizado).
- `read_text(self)`: Lee el texto detectado en voz alta.
- `readCurrentLetter(self)`: Maneja el estado de lectura automática según la configuración del selector.
- `speak_text(self, text)`: Convierte el texto en habla y ajusta la velocidad según la configuración.
- `reset_textBox(self)`: Reinicia el cuadro de texto para las letras detectadas.
- `use_yolo_algo(self, frame)`: Realiza la detección de lenguaje de señas mediante YOLO y actualiza la interfaz.
- `use_algoritmo(self, frame)`: Realiza la detección de lenguaje de señas mediante un algoritmo personalizado y actualiza la interfaz.

## Ejecución de la Aplicación

Se instancia la clase `CameraApp` y se inicia la interfaz gráfica junto con el bucle de la cámara.

```python
# Set your camera source (use 0 for default camera)
video_source = 0

root = tk.Tk()
app = CameraApp(root, "Camera App", video_source)
```

markdown
Copy code
# Aplicación de Cámara con Interfaz Gráfica

Este script en Python utiliza la biblioteca Tkinter para crear una aplicación de cámara con interfaz gráfica. La aplicación captura un flujo de video de la cámara, realiza la detección de lenguaje de señas mediante el modelo YOLO o un algoritmo personalizado, y proporciona funcionalidades adicionales como la lectura de texto y ajustes de velocidad de habla.

## Clase `CameraApp`

La clase `CameraApp` incluye métodos para inicializar la aplicación y configurar la interfaz, así como funciones para manejar eventos como cambiar entre algoritmos, leer texto y mostrar la detección en tiempo real. Se utiliza threading para ejecutar el bucle de la cámara en segundo plano y garantizar un rendimiento suave de la interfaz.

### Métodos Principales

- `__init__(self, window, window_title, video_source=0)`: Inicializa la aplicación y la interfaz.
- `camera_loop(self)`: Bucle principal para capturar y procesar los fotogramas de la cámara.
- `change_algorithm(self)`: Cambia entre los algoritmos de detección (YOLO o personalizado).
- `read_text(self)`: Lee el texto detectado en voz alta.
- `readCurrentLetter(self)`: Maneja el estado de lectura automática según la configuración del selector.
- `speak_text(self, text)`: Convierte el texto en habla y ajusta la velocidad según la configuración.
- `reset_textBox(self)`: Reinicia el cuadro de texto para las letras detectadas.
- `use_yolo_algo(self, frame)`: Realiza la detección de lenguaje de señas mediante YOLO y actualiza la interfaz.
- `use_algoritmo(self, frame)`: Realiza la detección de lenguaje de señas mediante un algoritmo personalizado y actualiza la interfaz.

## Ejecución de la Aplicación

Se instancia la clase `CameraApp` y se inicia la interfaz gráfica junto con el bucle de la cámara.

```python
# Set your camera source (use 0 for default camera)
video_source = 0

root = tk.Tk()
app = CameraApp(root, "Camera App", video_source)
```
Este script proporciona una aplicación básica con detección de lenguaje de señas en tiempo real y funcionalidades de lectura de texto. Puedes personalizar y expandir según tus necesidades específicas.
