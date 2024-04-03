#Importamos los modulos necesarios para realizar las operaciones
from email.message import EmailMessage
import ssl
import smtplib

#Construimos los elementos necesarios para montar el email
email_emisor = 'Aquí debeis incluir vuestro email'
email_contrasena = 'Aquí debeis incluir la contraseña' # esta contraseña se tiene que generar en el google accounts para tener una contraseña para app de terceros
email_receptor = 'El receptor' # Este será el destinatario

asunto = 'Debe ser el asunto'
cuerpo = """
Cuerpo
"""
#Monstage del email
em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

#Seguridad extra
contexto = ssl.create_default_context()

# A partir del servicio smtp nos logearemos como los datos de arriba
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())