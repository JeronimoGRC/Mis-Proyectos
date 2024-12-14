import yt_dlp

def Download(link,ruta):
    ydl_opt = {
        'outtmpl':ruta+'%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        ydl.download([link])
            
link = input("Pega tu link de youtube aquí, URL: ")
pregunta = input("¿Es música(Musica) o memo(Memo)? ")

if pregunta.upper() == "MUSICA":
    ruta = "C:/Users/Usuario/Desktop/Jero/"
elif pregunta.upper() == "MEMO":
    ruta = "C:/Users/Usuario/Desktop/Jero/Memos/"

Download(link,ruta)
