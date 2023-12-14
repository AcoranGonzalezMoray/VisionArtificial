# Practica 6
En esta práctica hemos desarollado una interfaz gráfica usando la libería Tkinter que tiene implementado las siguientes funcioanlidades:

## Autentificación Biométrica (Iniciar Sessión/Registrarse)
En el proyecto, hemos utilizado la función ```iniciar_sesion()``` utiliza un hilo (login_thread) para ejecutar el proceso de inicio de sesión en segundo plano, evitando que la interfaz se congele. El reconocimiento facial se realiza mediante la llamada a la misma función, que contiene  la lógica de verificación biométrica.

Para el registro biométrico, se utiliza la función ```registrarse_con_nombre()```, que guarda la imagen con el nombre de usuario proporcionado. 

## Mostrar datos del perfil del usuario
La función ```initUser()``` se encarga de mostrar la información del perfil del usuario. Utiliza la biblioteca **DeepFace** para analizar la foto de perfil y mostrar detalles como el nombre, edad, género, emoción, etc.

## Obtener tus propios albumenes de imagenes
El código proporciona funcionalidad para cargar y mostrar imágenes en el álbum del usuario. La función ```load_and_display_images()``` toma la ruta de la carpeta del usuario y carga las imágenes almacenadas en esa carpeta, mostrándolas en el canvas. Esto  permite visualizar las propias imágenes del álbum del usuario.

## Filtrado de imaganes basado en sus características físicas
El código proporciona dos funciones de filtrado: ```filtrar_por_emociones()``` y ```filtrar_por_genero()```. Ambas funciones crean un cuadro de diálogo para que el usuario ingrese la emoción o género por el cual desea filtrar las imágenes. Luego, filtran las imágenes según la emoción o género seleccionado y las muestran en el canvas.

<div align="center" >
  Pulsa la imagen para ver el video
  
  [![Watch the video](https://github.com/AcoranGonzalezMoray/VisionArtificial/blob/main/Pr%C3%A1ctica_6/otros/portada.png)](https://drive.google.com/file/d/1V6lpCB-0E18Nvy-fdrH4LP-ZR3IQYzOq/view?usp=sharing)
</div>

