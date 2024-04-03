#Importamos la biblioteca habiendo ejecutado antes en la línea de comandos 
#pip install pytube
from pytube import YouTube
import os

def Download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()#Obtenemos la resolución con mayor calidad del vídeo
    try:
        descarga = yt.download() #Ejecutamos la descarga habiendo pasado el link por parámetros
        #Con el modulo de os marcaremos un destino para los video que descarguemos 
        nombre_archivo = descarga.split("\\")[-1]
        destino = os.path.join("C:\\Users\\Usuario\\Desktop\\Jero\\Memos",nombre_archivo) #Esta será la ruta especificada
        #Es necesario que tenga las dobles barras invertidas
        os.rename(descarga,destino) #Movemos y renombramos el archivo
        print("Se ha incluido en la carpeta correctamente")
    except Exception as e:
        #Capturamos el error, en caso de que salte mostraremos el mensaje
        print("Hubo un error al descargar el video del URL proporcionado...",e) #Mostramos la excepción
    
    print("¡Descarga completada con éxito!")

# Pedimos al usuario en la línea de comandos ingresar el URL del video para descargar
link = input("Pega tu link de youtube aquí, URL: ")
 
# Descargamos el video
Download(link)