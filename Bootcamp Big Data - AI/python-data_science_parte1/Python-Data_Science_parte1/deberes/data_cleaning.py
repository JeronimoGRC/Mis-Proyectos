# Limpieza de Datos para el dataset de empleados
# ==============================================
# Objetivo: Limpiar y preparar el dataset generado con relaciones entre variables para análisis.

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import VarianceThreshold


# Paso 1: Cargar el dataset con las columnas especificadas
ruta_csv = 'C:/Users/Usuario/Desktop/Jero/Mis-Proyectos/Bootcamp Big Data - AI/python-data_science_parte1/Python-Data_Science_parte1/deberes/habitos_sueno.csv'
df = pd.read_csv(ruta_csv)

print("Filas antes de limpiar el dato: ", df.shape[0])

# Paso 2: Inspeccionar los datos antes de la limpieza
print("Información inicial del dataset:")
print(df.info())

print("\nResumen estadístico:")
print(df.describe())

# Paso 7: Limpieza y Codificación de variables categóricas
variables_categoricas = df.select_dtypes(
    include=['object']).columns.tolist()
print("Variables categóricas:", variables_categoricas)

df['Deporte_diario'] = df['Deporte_diario'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios
df['Tipo_alimentacion'] = df['Tipo_alimentacion'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios
df['Mes'] = df['Mes'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios
df['Estacion'] = df['Estacion'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios
df['Hora_acostarse'] = df['Hora_acostarse'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios
df['Hora_despertar'] = df['Hora_despertar'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios

for variable_categorica in variables_categoricas:
    conteo_categorias = df[variable_categorica].value_counts()
    print("Posibilidades únicas para la variable", variable_categorica)
    print(conteo_categorias)


df['Ha_bebido_alcohol'] = df['Ha_bebido_alcohol'].map(
    {True:'Si', False:'No'})
df.fillna("Desconocido", inplace=True)

for variable_categorica in variables_categoricas:
    conteo_categorias = df[variable_categorica].value_counts()
    # Filtrar solo las categorías que aparecen más de 20 veces
    categorias_validas = conteo_categorias[conteo_categorias > 20].index
    df = df[df[variable_categorica].isin(categorias_validas)]
    print("Posibilidades únicas para la variable", variable_categorica)
    print(df[variable_categorica].value_counts())

# Paso 8: Eliminar variables con baja varianza
selector = VarianceThreshold(threshold=0.01)
df_numeric = df.select_dtypes(include=[np.number])
selector.fit(df_numeric)
columnas_a_eliminar = df_numeric.columns[~selector.get_support()]
df = df.drop(columns=columnas_a_eliminar)
print("Columnas eliminadas por baja varianza:", columnas_a_eliminar.tolist())

print("Filas despues de limpiar el dato: ", df.shape[0])


# Paso 10: Guardar el dataset limpio
df.to_csv('C:/Users/Usuario/Desktop/Jero/Mis-Proyectos/Bootcamp Big Data - AI/python-data_science_parte1/Python-Data_Science_parte1/deberes/habitos_sueno_limpios.csv', index=False)
print("Limpieza de datos completada. Datos guardados en 'habitos_sueno_limpios.csv")
