from PIL import Image
import os

ruta = r"C:\\Users\\Usuario\\Desktop\\Jero\\Mis-Proyectos\\python Proyects\\imagenes"
# Obtenemos la lista de archivos en la carpeta
archivos = os.listdir(ruta)

eleccion = input("Quieres convertir a un png a jpg [1] o jpg a png [2]:[1/2] -> ")
if eleccion == "1":
# Filtramos los archivos con la extensión png
    imagenes = [archivo for archivo in archivos if archivo.endswith(".PNG")]

    # Ordenar la lista de imágenes por fecha de modificación (más reciente primero)
    imagenes.sort(key=lambda x: os.path.getmtime(os.path.join(ruta, x)), reverse=True)

    if imagenes: #Si hay imagenes en el array 
        nombre_imagen_mas_reciente = os.path.splitext(imagenes[0])[0]

    # Utilizamos la ruta y concatenamos el nombre de la imagen que acabamos de extraer
    imagen = Image.open(ruta+r"\\"+nombre_imagen_mas_reciente+".PNG")
    if imagen.mode != 'RGB':
        rgb_img = imagen.convert('RGB')
        rgb_img.save(ruta+r"\\"+f'{nombre_imagen_mas_reciente}_convertida.jpg')
    else:
        imagen.save(ruta+r"\\"+f'{nombre_imagen_mas_reciente}_convertida.jpg')
else:
    # Filtramos los archivos con la extensión png
    imagenes = [archivo for archivo in archivos if archivo.endswith(".PNG")]

    # Ordenar la lista de imágenes por fecha de modificación (más reciente primero)
    imagenes.sort(key=lambda x: os.path.getmtime(os.path.join(ruta, x)), reverse=True)

    if imagenes: #Si hay imagenes en el array 
        nombre_imagen_mas_reciente = os.path.splitext(imagenes[0])[0]

    # Utilizamos la ruta y concatenamos el nombre de la imagen que acabamos de extraer
    imagen = Image.open(ruta+r"\\"+nombre_imagen_mas_reciente+".jpg")
    if imagen.mode != 'RGB':
        rgb_img = imagen.convert('RGB')
        rgb_img.save(ruta+r"\\"+f'{nombre_imagen_mas_reciente}_convertida.png')
    else:
        imagen.save(ruta+r"\\"+f'{nombre_imagen_mas_reciente}_convertida.png')
