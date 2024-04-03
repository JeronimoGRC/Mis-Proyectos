#En mi caso he tenido que instalar la biblioteca pandas y la biblioteca lxml
import pandas as pd

#Lectura de la página web y almacenamos la tabla de esta dirección en una variable
simpson = pd.read_html('https://es.wikipedia.org/wiki/Anexo:Episodios_de_Los_Simpson')

print(simpson[1])