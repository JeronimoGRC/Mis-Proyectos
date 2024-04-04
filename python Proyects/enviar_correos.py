#Importamos los modulos necesarios para realizar las operaciones
from pathlib import Path
from email.message import EmailMessage
import ssl
import smtplib
import imghdr 

#Construimos los elementos necesarios para montar el email
email_emisor = 'Tu email' #Aquí deberás incluir tu email
email_contrasena = '' # esta contraseña se tiene que generar en el google accounts para tener una contraseña para app de terceros

email_receptor = input("Introduce un email -> ")

asunto = input('Rellena el asunto -> ')
cuerpo = input(""" Rellena el cuerpo""")
#Monstage del email
em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

#Adjuntar archivos
imagen_bool = input("¿Quieres adjuntar un archivo?[y/n] ")
if imagen_bool == "y":
    imagen = input("Adjuntar archivo: ")
    documento = Path(f'imagenes/{imagen}')
    with open(documento, 'rb') as file:
        datos_fichero = file.read() 
        tipo_fichero = imghdr.what(file.name) # Se extrae el tipo de archivo que es
        nombre_fichero = file.name #Definimos el nombre

#Con esta línea adjuntamos un el archivo 
em.add_attachment(datos_fichero, filename=nombre_fichero, subtype=tipo_fichero, maintype='image')

#Seguridad extra
contexto = ssl.create_default_context()

# A partir del servicio smtp nos logearemos como los datos de arriba
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())

print("¡Email enviado!")