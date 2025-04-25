import polars as pl

# Métodos más utilizados de la biblioteca polars:

# 1. pl.DataFrame():
# Crea un DataFrame de Polars a partir de datos estructurados.
df = pl.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis"],
    "Edad": [25, 30, 22],
    "Ciudad": ["Madrid", "Barcelona", "Valencia"]
})
print("DataFrame creado:")
print(df)

# 2. df.head(n):
# Devuelve las primeras n filas del DataFrame (por defecto, 5 filas).
print("\nPrimeras filas del DataFrame:")
print(df.head())

# 3. df.tail(n):
# Devuelve las últimas n filas del DataFrame (por defecto, 5 filas).
print("\nÚltimas filas del DataFrame:")
print(df.tail())

# 4. df.shape:
# Devuelve las dimensiones del DataFrame (filas, columnas).
print("\nDimensiones del DataFrame:")
print(df.shape)

# 5. df.columns:
# Devuelve los nombres de las columnas.
print("\nColumnas del DataFrame:")
print(df.columns)

# 6. df.select("columna"):
# Selecciona una columna específica.
print("\nSeleccionar la columna 'Nombre':")
print(df.select("Nombre"))

# 7. df.filter(df["columna"] > valor):
# Filtra filas que cumplen una condición.
print("\nFiltrar personas mayores de 25 años:")
print(df.filter(df["Edad"] > 25))

# 8. df.sort("columna", descending=True/False):
# Ordena el DataFrame por una columna.
print("\nOrdenar por edad de forma ascendente:")
print(df.sort("Edad"))

# 9. df.groupby("columna").agg(pl.count()):
# Agrupa datos según una columna y aplica una función de agregación.
print("\nContar cuántas personas hay en cada ciudad:")
print(df.groupby("Ciudad").agg(pl.count()))

# 10. df.drop("columna"):
# Elimina una o más columnas del DataFrame.
df_sin_edad = df.drop("Edad")
print("\nDataFrame sin la columna Edad:")
print(df_sin_edad)

# 11. df.null_count():
# Cuenta la cantidad de valores nulos en cada columna.
print("\nCantidad de valores nulos por columna:")
print(df.null_count())

# 12. df.fill_null("valor"):
# Reemplaza valores nulos por un valor específico.
df_filled = df.fill_null("Desconocido")
print("\nDataFrame con valores nulos reemplazados:")
print(df_filled)

# 13. df.with_columns():
# Agrega nuevas columnas o modifica las existentes.
df_modificado = df.with_columns((df["Edad"] + 5).alias("Edad_Modificada"))
print("\nDataFrame con nueva columna 'Edad_Modificada':")
print(df_modificado)

# 14. pl.read_csv("archivo.csv"):
# Carga un DataFrame desde un archivo CSV.
df_csv = pl.read_csv("archivo.csv")
print("\nDataFrame cargado desde CSV:")
print(df_csv.head())

# 15. df.write_csv("archivo.csv"):
# Guarda el DataFrame en un archivo CSV.
df.write_csv("archivo.csv")
print("\nDataFrame guardado en CSV")
