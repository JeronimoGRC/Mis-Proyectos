import pandas as pd

#Uso de Diccionarios con Pandas
materias = pd.Series({'Matemáticas':60, 'Física':75, 'Química':45})
materias[['Física','Química']]
print(materias)