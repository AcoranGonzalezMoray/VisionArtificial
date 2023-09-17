# Práctica 1 Anadonda
En este práctica hemos trabajado con Anaconda y OpenCV para cumplir una serie de tareas.
Antes de completar todas las tareas, tenemos que instalar los siguientes paquetes.
LUHFLIKHFLIKHFLIKFHLIU

## Tarea 1:  Crea una imagen, p.e. 800x800, con la textura del tablero de ajedrez
Para completar este trabajo, primeros hemos defindo las dimensiones de la imagén, a contunuación pintamos las casillas blancas (255) correspondientes sobre el fondo negro (0).
Este proceso, lo metemos en un bucle de doble for, para completar de está manera la imagen completa.
```python
#Dimensiones de la imagen a crear
Bancho = 800
Balto = 800
#Crea una imagen de un único plano, que se interpreta como nivel de gris (0 negro, 255 blanco)
gris_imgB = np.zeros((Bancho,Balto,1), dtype = np.uint8)

#Modifica un par de zonas rectangulares de la imagen
#gris_imgB[vertical,horizontal,0] 0 indica 1 plano, para coloes

filas = 8
columnas = 8
tamaño = 100

for fila in range(filas):
    for columna in range(columnas):
        if (fila+columna)%2==0:
            gris_imgB[fila*tamaño:fila*tamaño+tamaño,columna*tamaño:columna*tamaño+tamaño] = 255

#Muestra la imagen con matplotlib
#Es necesario especificar que el mapa de color usado es de grises
plt.imshow(gris_imgB, cmap='gray')
plt.show()
```
![image](https://github.com/AcoranGonzalezMoray/VisionArtificial/assets/99484843/52ec972a-c715-441e-9461-d5340e90899e)

## Tarea 2: Crear una imagen estilo Mondrian
Esta imagen está generado de forma estática y se han puesto las lineas de forma manual. Una vez que hemos pintado las lineas, contiuamos con rellenar los cuadros con
su color correspondiente.

```python
#Dimensiones de la imagen a crear
Cancho = 800
Calto = 800
#Crea una imagen de tres planos
gris_imgC = np.zeros((Cancho,Calto,3), dtype = np.uint8)

gris_imgC.fill(255)

#Lineas Verticales
gris_imgC[0:800,24:46]      =0 
gris_imgC[0:800,700:722]    =0
gris_imgC[0:800,178:200]    =0 
gris_imgC[0:500,378:400]    =0
gris_imgC[250:800,528:550]  =0 

#Lineas Horizontales
gris_imgC[250:272,0:800]    =0 
gris_imgC[500:522,0:700]    =0 
gris_imgC[700:722,24:800]   =0


#Colores Formas
gris_imgC[0:250,46:178]    = [255,255,0] 
gris_imgC[0:250,200:378]    = [0,0,255] 
gris_imgC[0:250,400:700]    = [255,0,0] 
gris_imgC[272:500,550:700]    = [0,0,255] 
gris_imgC[522:700,200:528]    = [255,0,0] 
gris_imgC[722:800,200:528]    = [255,255,0] 
gris_imgC[722:800,46:178]    = [0,0,255] 

#Muestra la imagen con matplotlib
#No es necesario especificar que el mapa de color usado es de grises
plt.imshow(gris_imgC)
plt.show()
```
![image](https://github.com/AcoranGonzalezMoray/VisionArtificial/assets/99484843/462d4e96-5a57-4217-bf38-55c37dbd7af8)

## Tarea 3: Resuelve una de las tareas previas (a elegir) con las funciones de dibujo de OpenCV
Para esta tarea, hemos simplemente recreado las tareas propuestas más arriba usando OpenCV. Primero, hemos recreado el tablero de ajedrez de la siguiente manera:

```python
#Crea una imagen con tres planos
color_img = np.zeros((800,800,3), dtype = np.uint8)

#Rectángulo con grosor 2
#cv2.rectangle(color_img,(10,10),(ancho-10,int(alto/2)),(0,255,0),2)
#Rectángulo relleno
#cv2.rectangle(color_img,(20,20),(60,40),(0,255,0),-1)


filas = 8
columnas = 8
tamaño = 100

for fila in range(filas):
    for columna in range(columnas):
        if (fila+columna)%2==0:
            cv2.rectangle(color_img, (columna * tamaño, fila * tamaño), ((columna + 1) * tamaño, (fila + 1) * tamaño), (255, 255, 255), -1)
            #gris_imgB[fila*tamaño:fila*tamaño+tamaño,columna*tamaño:columna*tamaño+tamaño,0] = 255


#Visualiza sin especificar el mapa de color gris
plt.imshow(color_img) 
plt.show()


#Salva la imagen resultante a disco
cv2.imwrite('imagenCVAjedrez.jpg', color_img)
```
![image](https://github.com/AcoranGonzalezMoray/VisionArtificial/assets/99484843/536f1f64-24a6-47be-935f-ffdce8c9fdcc)

Y a continuación, hemos recreado la otra tarea de la imgen estilo Mondrian, y hemos obtenido lo siguiente como resultado:

```python
#Crea una imagen con tres planos
color_img = np.zeros((800,800,3), dtype = np.uint8)
color_img.fill(255)

Lancho = 800
Lalto = 800

#Rectángulo relleno
cv2.rectangle(color_img,(200,200),(20,0),(0,0,255), -1)
cv2.rectangle(color_img,(360,200),(750,0),(255,255,0), -1)
cv2.rectangle(color_img,(200,450),(20,200),(255,0,0), -1)
cv2.rectangle(color_img,(360,450),(200,750),(0,0,255), -1)
cv2.rectangle(color_img,(750,600),(360,750),(255,255,0), -1)
cv2.rectangle(color_img,(800,750),(360,800),(255,0,0), -1)
cv2.rectangle(color_img,(800,200),(750,750),(0,0,255), -1)
cv2.rectangle(color_img,(20,800),(0,200),(255,255,0), -1)

#Línea roja vertical de grosor 3
cv2.line(color_img,(int(20),0),(int(20),800),(0,0,0),13)
cv2.line(color_img,(int(200),0),(int(200),800),(0,0,0),13)
cv2.line(color_img,(int(750),0),(int(750),750),(0,0,0),13)
cv2.line(color_img,(int(360),0),(int(360),800),(0,0,0),13)

cv2.line(color_img,(int(800),200),(int(0),200),(0,0,0),13)
cv2.line(color_img,(int(360),450),(int(20),450),(0,0,0),13)
cv2.line(color_img,(int(800),200),(int(0),200),(0,0,0),13)
cv2.line(color_img,(int(800),750),(int(200),750),(0,0,0),13)
cv2.line(color_img,(int(750),600),(int(360),600),(0,0,0),13)


#Visualiza sin especificar el mapa de color gris
plt.imshow(color_img) 
plt.show()
```

![image](https://github.com/AcoranGonzalezMoray/VisionArtificial/assets/99484843/8ce70760-770f-4330-94c3-ae3a3fb112be)

## Tarea 4: Modifica de alguna forma los valores de un plano de la imagen
en el siguiente código mostrado más abajo



