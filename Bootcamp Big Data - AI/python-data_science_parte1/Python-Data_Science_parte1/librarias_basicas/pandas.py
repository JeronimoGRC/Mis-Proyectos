import pandas as pd

# Métodos más utilizados de la biblioteca pandas:

# 1. pd.DataFrame():
# Crea un DataFrame a partir de datos estructurados.

datos = {
    'Nombre': ['Ana', 'Carlos', 'Luis'],
    'Edad': [25, 30, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(datos)
print("DataFrame creado:")
print(df)

# 2. pd.read_csv('archivo.csv'):
# Carga un DataFrame desde un archivo CSV.
df_csv = pd.read_csv('archivo.csv')
print("\nDataFrame cargado desde CSV:")
print(df_csv.head())

# 3. pd.read_excel('archivo.xlsx'):
# Carga un DataFrame desde un archivo Excel.
df_excel = pd.read_excel('archivo.xlsx')
print("\nDataFrame cargado desde Excel:")
print(df_excel.head())

# 4. df.to_csv('archivo.csv', index=False):
# Guarda el DataFrame en un archivo CSV sin índices.
df.to_csv('archivo.csv', index=False)
print("\nDataFrame guardado en CSV")

# 5. df.to_excel('archivo.xlsx', index=False):
# Guarda el DataFrame en un archivo Excel.
df.to_excel('archivo.xlsx', index=False)
print("\nDataFrame guardado en Excel")

# 6. df.head(n):
# Devuelve las primeras n filas del DataFrame (por defecto, 5 filas).
print("\nPrimeras filas del DataFrame:")
print(df.head())

# 7. df.tail(n):
# Devuelve las últimas n filas del DataFrame (por defecto, 5 filas).
print("\nÚltimas filas del DataFrame:")
print(df.tail(2))

# 8. df.sample(n):
# Muestra n filas aleatorias del DataFrame.
print("\nMuestra aleatoria de 2 filas:")
print(df.sample(2))

# 9. df.info():
# Muestra información general del DataFrame.
print("\nInformación del DataFrame:")
df.info()

# 10. df.describe():
# Genera estadísticas descriptivas de las columnas numéricas.
print("\nEstadísticas descriptivas:")
print(df.describe())

# 11. df.shape:
# Devuelve las dimensiones del DataFrame (filas, columnas).
print("\nDimensiones del DataFrame:")
print(df.shape[1])

# 12. df.columns:
# Devuelve los nombres de las columnas.
print("\nColumnas del DataFrame:")
print(df.columns)

# 13. df.index:
# Devuelve el índice del DataFrame.
print("\nÍndice del DataFrame:")
print(df.index)

# 14. df.loc[row, col]:
# Accede a un elemento del DataFrame usando etiquetas.
print("\nAcceder a la edad de Carlos:")
print(df.loc[1, 'Edad'])

# 15. df.iloc[row, col]:
# Accede a un elemento del DataFrame usando índices numéricos.
print("\nAcceder al primer elemento de la primera fila:")
print(df.iloc[0, 0])

# 16. df['columna']:
# Selecciona una columna como una Serie de pandas.
print("\nSeleccionar la columna 'Nombre':")
print(df['Nombre'])

# 17. df[['columna1', 'columna2']]:
# Selecciona múltiples columnas.
print("\nSeleccionar 'Nombre' y 'Edad':")
print(df[['Nombre', 'Edad']])

# 18. df[df['columna'] condición]:
# Filtra filas que cumplen una condición.
print("\nFiltrar personas mayores de 25 años:")
print(df[df['Edad'] > 25])

# 19. df.sort_values(by='columna', ascending=True/False):
# Ordena el DataFrame por una columna.
print("\nOrdenar por edad de forma ascendente:")
print(df.sort_values(by='Edad'))

# 20. df.groupby('columna').agg_func():
# Agrupa datos según una columna y aplica una función de agregación.
print("\nContar cuántas personas hay en cada ciudad:")
print(df.groupby('Ciudad').size())

# 21. df.drop(columns=['columna']):
# Elimina una o más columnas del DataFrame.
df_sin_edad = df.drop(columns=['Edad'])
print("\nDataFrame sin la columna Edad:")
print(df_sin_edad)

# 22. df.isnull().sum():
# Verifica valores nulos en el DataFrame.
print("\nCantidad de valores nulos por columna:")
print(df.isnull().sum())

# 23. df.fillna(valor):
# Reemplaza valores nulos por un valor específico.
df_filled = df.fillna('Desconocido')
print("\nDataFrame con valores nulos reemplazados:")
print(df_filled)

# 24. df.dropna():
# Elimina filas con valores nulos.
df_sin_nulos = df.dropna()
print("\nDataFrame sin valores nulos:")
print(df_sin_nulos)

# 25. df.duplicated():
# Devuelve un booleano indicando si una fila es duplicada.
print("\nFilas duplicadas en el DataFrame:")
print(df.duplicated())

# 26. df.drop_duplicates():
# Elimina filas duplicadas.
df_sin_duplicados = df.drop_duplicates()
print("\nDataFrame sin filas duplicadas:")
print(df_sin_duplicados)

# 27. df.memory_usage():
# Muestra la cantidad de memoria utilizada por cada columna.
print("\nUso de memoria del DataFrame:")
print(df.memory_usage())
