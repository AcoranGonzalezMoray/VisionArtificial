# Práctica 2

## Tarea 1 
En esta tarea se realizó un procesamiento de imágenes utilizando las técnicas de Sobel y Canny para la detección de bordes. Luego, se contaron los píxeles blancos por filas y columnas en la imagen resultante de Canny, calculando el máximo y determinando las filas y columnas que superan el 95% de ese máximo. Finalmente, se resaltaron visualmente estas filas y columnas en la imagen. Algunas de las funciones usadas fueron:
<ul>
<li>cv2.imread('mandril.jpg'): Para cargar una imagen.</li>
<li>cv2.cvtColor(img, cv2.COLOR_BGR2GRAY): Para convertir la imagen a escala de grises.</li>
<li>cv2.Canny(gris, 100, 200): Para aplicar el operador de Canny y detectar bordes.</li>
<li>cv2.reduce(canny, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32SC1): Para reducir la imagen y contar píxeles por columnas y filas.</li>
<li>cv2.imshow(): Para mostrar imágenes en ventanas.</li>
<li>plt.imshow(): Para mostrar imágenes utilizando matplotlib.</li>
<li>plt.plot(): Para crear gráficos.</li>
</ul>

## Tarea 2
En esta tarea se cargó una imagen en escala de grises, se aplicó un suavizado Gaussiano y se calculó el gradiente en ambas direcciones (horizontal y vertical) utilizando el operador Sobel. Se ajustó la escala de las imágenes de Sobel y se mostraron las imágenes resultantes antes y después de la escala.Algunas de las funciones usadas fueron:
<ul>
<li>cv2.imread('98.jpg', cv2.IMREAD_GRAYSCALE): Para cargar una imagen en escala de grises.</li>
<li>cv2.GaussianBlur(): Para aplicar suavizado Gaussiano.</li>
<li>cv2.Sobel(): Para calcular gradientes con el operador Sobel.</li>
<li>cv2.convertScaleAbs(): Para ajustar la escala de las imágenes de Sobel.</li>
<li>plt.subplot(): Para crear subplots y mostrar varias imágenes en una figura.</li>
</ul>

## Tarea 3 
En esta tarea, se aplicó umbralización a la imagen resultante de Sobel y se realizó un conteo de píxeles blancos por filas y columnas de la imagen umbralizada. Se calcularon los máximos por filas y columnas y se determinaron las filas y columnas por encima del 95% de esos máximos. Luego, se resaltaron visualmente estas filas y columnas en la imagen umbralizada.Algunas de las funciones usadas fueron:
<ul>
<li>np.uint8(): Para convertir la imagen a 8 bits..</li>
<li>cv2.threshold(): Para aplicar umbralización a la imagen..</li>
<li>np.sum(): Para contar píxeles blancos por filas y columnas..</li>
</ul>

## Tarea 4 
Algunos de los comportamientos aplicadas sobre la webcam pueden ser:

1.Detección de bordes con Sobel y Canny: Puedes mostrar cómo las funciones de detección de bordes de Sobel y Canny resaltan los bordes de objetos en la imagen de la webcam en tiempo real.

2.Filtrado en tiempo real: Experimenta con diferentes umbrales y métodos de umbralización para resaltar características específicas en la imagen de la webcam mientras se actualiza en tiempo real.

3.Seguimiento de objetos en tiempo real y contorneado: Implementa un sistema de seguimiento de objetos en la imagen de la webcam utilizando las funciones de conteo y umbralización. Muestra cómo el sistema puede seguir objetos en movimiento.

4.Comparación de resultados: Muestra y compara los resultados obtenidos a partir de las funciones de Sobel y Canny en tiempo real. Destaca las diferencias en la detección de bordes y cómo se comportan en diferentes escenarios.

5.Superposición de información en tiempo real: Agrega información adicional, como coordenadas de objetos detectados o valores de píxeles relevantes, superpuestos en la imagen de la webcam en tiempo real.

En nustro caso nos decantamos por el seguimiento de objetos oscuros

## Tarea 5 
Aqui creamos un proyecto llamado "Virtual Artistic Mirror" con  2 versiones basadas en la sustraccion de fondo:

Version 1: Se utilizó el algoritmo de sustracción de fondo para crear un lienzo virtual. Se implementó la capacidad de "pintar" una forma geometrica en el lienzo virtual con gestos y movimientos capturados por la cámara

Version 2: Version mejorada que permite dibujar con mas precision a travez de un objeto amarillo

