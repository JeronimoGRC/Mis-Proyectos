# Limpieza de Datos para el dataset de empleados
# ==============================================
# Objetivo: Limpiar y preparar el dataset generado con relaciones entre variables para análisis.

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import VarianceThreshold
#from modulos import utils

def convertir_fecha(fecha):
    """convertir fecha con valor erroneo custom

    Args:
        fecha (str): valor inicial del string

    Returns:
        date/str: resultado de la transformacion
    """
    try:
        # Intentar conversión
        return pd.to_datetime(fecha, errors='raise')
    except Exception:
        # Si falla, devolver mensaje de error con el valor original
        return f"ERROR - ({fecha})"


# Paso 1: Cargar el dataset con las columnas especificadas
ruta_csv = 'C:/Users/Usuario/Desktop/Jero/Mis-Proyectos/Bootcamp Big Data - AI/python-data_science_parte1/Python-Data_Science_parte1/flujo_data_science/datos_empleados_sucios.csv'
df = pd.read_csv(ruta_csv)

print("Filas antes de limpiar el dato: ", df.shape[0])

# Paso 2: Inspeccionar los datos antes de la limpieza
print("Información inicial del dataset:")
print(df.info())

print("\nResumen estadístico:")
print(df.describe())

# Paso 3: Tratamiento de Fechas

# Convertir la columna de fechas a datetime
df['Fecha_Contratacion'] = df['Fecha_Contratacion'].apply(
    convertir_fecha)
df['Fecha_Fin_Contrato'] = df['Fecha_Fin_Contrato'].apply(
    convertir_fecha)


# Seleccionar solo las columnas con tipo datetime
columnas_fechas = df.select_dtypes(include=['datetime']).columns
print("Columnas con fechas:", list(columnas_fechas))


# Detectar valores incorrectos en las fechas (NaT)
errores_fecha_contratacion_NaT = df[df['Fecha_Contratacion'].isna()]
errores_fecha_contratacion_type = df[df['Fecha_Contratacion'].astype(
    str).str.startswith("ERROR")]
errores_fecha_fin_contrato_type = df[df['Fecha_Fin_Contrato'].astype(
    str).str.startswith("ERROR")]


errores_fecha_total = pd.concat(
    [errores_fecha_contratacion_NaT, errores_fecha_contratacion_type,
     errores_fecha_fin_contrato_type], ignore_index=True)
print("Numero Filas con errores en en fechas:",
      errores_fecha_total.shape[0])

# Guardar el dataset valores erroneos
errores_fecha_total.to_csv(
    'flujo_data_science/datos_fechas_erroneas.csv', index=False)

# Descartamos valores erroneos
df = df.merge(errores_fecha_total, how='left', indicator=True).query(
    '_merge == "left_only"').drop(columns=['_merge'])

# Limpiamos casos con fecha de inicio despues que la fecha de fin
df = df[((df['Fecha_Fin_Contrato'].isna()) | (
    df['Fecha_Contratacion'] < df['Fecha_Fin_Contrato']))]

# Limpiamos Activos con fecha fin e inactivos sin fecha de inicio
df = df[~((df['Activo'] == 0) & df['Fecha_Fin_Contrato'].isna())]
df = df[~((df['Activo'] == 1) & df['Fecha_Fin_Contrato'].notna())]


# Nos quedamos en el año de las fechas
df['Anio_Contratacion'] = pd.to_datetime(
    df['Fecha_Contratacion'], errors='coerce').dt.year
df['Anio_Fin_Contrato'] = pd.to_datetime(
    df['Fecha_Fin_Contrato'], errors='coerce').dt.year.astype('Int64')

# Si el empleado sigue activo, usar 2025 como fecha de referencia
df['Anios_Trabajo'] = np.where(df['Activo'] == 1, 2025 - df['Anio_Contratacion'],
                               df['Anio_Fin_Contrato'] - df['Anio_Contratacion'])


df = df.drop(columns=['Fecha_Contratacion', 'Fecha_Fin_Contrato'])


# Paso 4: Eliminar valores no válidos por Edad

# Edad y años de experiencia deben cumplir que años de experiencia <= edad - 18
df = df[df['Anios_Experiencia'] <= (df['Edad'] - 18)]
print(df.shape[0])

# Paso 5: Eliminar valores nulos
df = df.dropna(
    subset=[col for col in df.columns if col != 'Anio_Fin_Contrato'])

# Paso 6: Eliminar duplicados basados en ID del empleado
df = df.drop_duplicates(subset=['ID'], keep='first')

# Paso 7: Limpieza y Codificación de variables categóricas
variables_categoricas = df.select_dtypes(
    include=['object', 'category']).columns.tolist()
print("Variables categóricas:", variables_categoricas)

df['Categoria'] = df['Categoria'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios
df['Departamento'] = df['Departamento'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios
df['Sucursal'] = df['Sucursal'].astype(str).str.strip(
).str.lower()  # Convertir a minúsculas y quitar espacios


for variable_categorica in variables_categoricas:
    conteo_categorias = df[variable_categorica].value_counts()
    print("Posibilidades únicas para la variable", variable_categorica)
    print(conteo_categorias)


df['Categoria'] = df['Categoria'].replace(
    {'s': 'senior', 'm': 'manager', 'j': 'junior', 'junior.': 'junior', 'b': 'becario', 'd': 'director'})
df['Departamento'] = df['Departamento'].replace(
    {'hr': 'rrhh', 'finance': 'finanzas', 'vent@s': 'ventas', 'markeing': 'marketing'})
df['Sucursal'] = df['Sucursal'].replace(
    {'e': 'este', 'o': 'oeste', 'w': 'oeste', 'n': 'Norte', 's': 'sur', 'c': 'centro'})


for variable_categorica in variables_categoricas:
    conteo_categorias = df[variable_categorica].value_counts()
    # Filtrar solo las categorías que aparecen más de 20 veces
    categorias_validas = conteo_categorias[conteo_categorias > 20].index
    df = df[df[variable_categorica].isin(categorias_validas)]
    print("Posibilidades únicas para la variable", variable_categorica)
    print(df[variable_categorica].value_counts())


# NO Convertimos las variables categoricas en.
label_encoder = LabelEncoder()
df['Categoria'] = label_encoder.fit_transform(df['Categoria'])
df['Departamento'] = label_encoder.fit_transform(df['Departamento'])
df['Sucursal'] = label_encoder.fit_transform(df['Sucursal'])


# Paso 8: Eliminar variables con baja varianza
selector = VarianceThreshold(threshold=0.01)
df_numeric = df.select_dtypes(include=[np.number])
selector.fit(df_numeric)
columnas_a_eliminar = df_numeric.columns[~selector.get_support()]
df = df.drop(columns=columnas_a_eliminar)
print("Columnas eliminadas por baja varianza:", columnas_a_eliminar.tolist())


print("Filas despues de limpiar el dato: ", df.shape[0])

# Paso 9: Limpiar formatos de variables
df['Anios_Trabajo'] = df['Anios_Trabajo'].astype('Int64')
df['Proyectos_Completados'] = df['Proyectos_Completados'].astype('Int64')

# Paso 10: Guardar el dataset limpio
df.to_csv('C:/Users/Usuario/Desktop/Jero/Mis-Proyectos/Bootcamp Big Data - AI/python-data_science_parte1/Python-Data_Science_parte1/flujo_data_science/datos_empleados_limpios.csv', index=False)
print("Limpieza de datos completada. Datos guardados en 'datos_empleados_limpios.csv'")
