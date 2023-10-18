# Tareas con Imágenes de Monedas

## Tarea 1: Filtrado de Contornos en una Imagen de Monedas

**Descripción:**

En esta tarea, se lleva a cabo el procesamiento de una imagen que contiene monedas, con el objetivo de filtrar los contornos que corresponden a monedas y mostrar el número total de monedas presentes en la imagen. Para realizar esto, se siguen los siguientes pasos:

1. Se lee la imagen y se la convierte a escala de grises.

2. Se aplica un umbral para obtener una imagen binaria que destaque los objetos.

3. Se encuentran todos los contornos en la imagen, tanto los externos como los internos.

4. Se obtienen únicamente los contornos externos, que corresponden a las monedas.

5. Se dibujan los contornos tanto en la imagen original como en una imagen vacía.

6. Se calcula la relación entre el área y el cuadrado del perímetro de cada contorno para filtrar las monedas, considerando un umbral de redondez.

7. Se determina el valor de cada moneda en función de su diámetro.

8. Se muestra la cantidad total de monedas y sus diámetros.

**Resultados:**

Se muestra una imagen con los contornos externos, una imagen con los contornos externos rellenos y una imagen con los contornos redondos después de aplicar el filtro de redondez. Además, se imprime el número total de monedas en la imagen y los diámetros de las monedas detectadas.

![Todos los contornos](imagen1.png)

![Sólo contornos externos](imagen2.png)

![Externos rellenos](imagen3.png)

![Contornos Redondos Con filtro](imagen4.png)

**Número de Monedas:** 8

**Diametros:** [87.64540100097656, 93.00223541259766, 84.38028717041016, 91.0156478881836, 93.7452392578125, 102.72354125976562, 101.63707733154297, 94.02146911621094]


## Tarea 2: Cálculo de Cantidad de Dinero en Imágenes de Monedas

**Descripción:**

En esta tarea, se procesan imágenes de monedas que pueden contener monedas solapadas y no solapadas. El objetivo es identificar una moneda de un euro en la imagen y calcular la cantidad total de dinero presente en la imagen.

Se proporcionan dos versiones de la tarea: una sin el uso de HoughCircles y otra con HoughCircles. En ambas versiones, se sigue el siguiente proceso:

1. Se lee la imagen y se aplica un procesamiento previo, que incluye la conversión a escala de grises y suavizado.

2. En la versión sin HoughCircles, se permite al usuario seleccionar una moneda haciendo clic en ella, lo que actualiza la escala utilizada para calcular los valores de las monedas. Además, se almacenan los diámetros de todas las monedas en una lista.

3. En la versión con HoughCircles, se detectan automáticamente los círculos en la imagen, se selecciona uno de ellos y se calcula la escala y los diámetros de todas las monedas detectadas.

4. Se calcula el valor correspondiente a cada moneda en función de su diámetro y se suma para obtener el valor total de dinero en la imagen.

**Resultados:**

Se muestra la imagen con los contornos redondos después de aplicar el filtro de redondez en la versión sin HoughCircles. En ambas versiones, se imprime el diámetro de la moneda seleccionada, la escala actualizada, el número de monedas detectadas, los diámetros de todas las monedas y los valores correspondientes de las monedas. Finalmente, se muestra el valor total de dinero en la imagen.

**Versión 1: SIN HOUGH**

- Diámetro de la moneda seleccionada: 138 px
- Escala actualizada: 24.2 / 138 = 0.17572463768115942
- Número de Monedas: 8
- Diametros de todas las monedas: [126.4000015258789, 134.1999969482422, 130.60000610351562, 110.5999984741211, 121.19999694824219, 113.4000015258789, 139.60000610351562, 114.5999984741211] px
- Valores de las monedas con escala aplicada: [22.21159447103307, 23.58224584054256, 22.949638753697492, 19.435144659401715, 21.297825550687485, 19.927174181177996, 24.531160492827926, 20.13804321012635]
- Valor Total: 3.050

**Versión 2: CON HOUGH**

- Diámetro de la moneda seleccionada: 138 px
- Escala actualizada: 24.2 / 138 = 0.17572463768115942
- Número de Monedas: 8
- Diametros de todas las monedas: [126.400
