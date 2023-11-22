# Práctica 5

## Objetivo
El objetivo de esta práctica es realizar la detección de matrículas y su contenido en imágenes y videos, utilizando el modelo YOLO (You Only Look Once) para la detección de objetos, y aplicando técnicas de procesamiento de imágenes y reconocimiento óptico de caracteres (OCR).

## Versión 1: Deteccion de matricula y contenido sin yolo sobre imagen
En esta versión, se lleva a cabo la detección de matrículas y su contenido en una imagen sin utilizar YOLO. En lugar de ello, se aplican técnicas de procesamiento de imágenes, como el desenfoque gaussiano, la detección de bordes mediante el operador Canny, y la aproximación de contornos para identificar las matrículas. Posteriormente, se utiliza la biblioteca EasyOCR para el reconocimiento óptico de caracteres y extraer el texto de las matrículas.

Como resultado se obtuvo lo siguiente:
<img src="https://github.com/AcoranGonzalezMoray/VisionArtificial/blob/main/Pr%C3%A1ctica_5/Filter/filtrado_con_matriculas_ocr.jpg?raw=true">

## Versión 2: Entrenamiento con base modelo yolo
En esta versión, se entrena un modelo YOLO específicamente para la detección de matrículas. Se utiliza el conjunto de datos proporcionado por Roboflow para el entrenamiento del modelo. Se especifica la arquitectura del modelo YOLO y se configuran los parámetros necesarios. Luego, se realiza el entrenamiento del modelo con el conjunto de datos etiquetado.

Código usado:
```
from ultralytics import YOLO
# Inicializar el modelo YOLO pre-entrenado
model = YOLO('yolov8n')  # Puedes especificar 'yolov5s', 'yolov5m', 'yolov5l', o 'yolov5x'

# Cargar datos y comenzar el entrenamiento
results = model.train(data='data.yaml', epochs=5, imgsz=640, device='mps')
```

## Versión 2.1: Deteccion de matricula y contenido con yolo sobre imagen
Después del entrenamiento del modelo YOLO en la Versión 2, se aplica la detección de matrículas y su contenido en una imagen utilizando el modelo preentrenado. Se utiliza el modelo YOLO entrenado específicamente para matrículas, y se muestra el resultado de la detección en la imagen y su contenido.

Como resultado se obtuvo lo siguiente:
<img src="https://github.com/AcoranGonzalezMoray/VisionArtificial/blob/main/Pr%C3%A1ctica_5/Filter/1_detected_plates.jpg?raw=true">



## Versión 2.2: Deteccion de matricula y contenido sin yolo sobre video
En esta versión, se realiza la detección de matrículas y su contenido en un video sin utilizar YOLO. Se utiliza nuevamente el enfoque de procesamiento de imágenes empleado en la Versión 2.1, pero aplicado a cada fotograma del video. Se emplean técnicas de procesamiento y OCR para identificar y extraer información de las matrículas en el video.

<video controls width="640" height="360">
    <source src="https://github.com/AcoranGonzalezMoray/VisionArtificial/blob/main/Pr%C3%A1ctica_5/Filter%20mp4/video_con_detecciones.mp4?raw=true" type="video/mp4">
    Tu navegador no soporta la etiqueta de video.
</video>





## Conclusion 
la práctica proporcionó una visión integral de la detección de matrículas, desde métodos tradicionales de procesamiento de imágenes hasta el uso de modelos avanzados como YOLO. La combinación de técnicas mostró cómo abordar desafíos específicos y adaptarse a diferentes contextos, destacando la versatilidad y eficacia de las soluciones implementadas.
