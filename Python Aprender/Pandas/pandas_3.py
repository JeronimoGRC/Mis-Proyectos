from numpy import indices
import pandas as pd

diccionario = {'Matemáticas':6, 'Física':8, 'Química':4}
serie = pd.Series(diccionario)

# print(serie[serie > 6])  La salida son los valores que tengan más de 6
# print(serie.sort_values()) Ordena los datos de manera ascendente
# print(serie.sort_index(ascending=True)) Se ordenan alfabeticamente ascendente,
# si pones False se ordenará descendente

data = 5
serie_new = pd.Series(data, index=[0,1,2,3,4,5]) 
# Copia el dato y le añade los indices que hay en la tabla 
data_list = ['Messi', 'CR7', 'Falcao']
indices = ['BarÇa', 'Real Madrid', 'Atleti no se hable más']

futibol = pd.Series(index=indices,data=data_list) 
#Creamos un array de indices y uno de datos para después crear una tabla 
print(futibol)