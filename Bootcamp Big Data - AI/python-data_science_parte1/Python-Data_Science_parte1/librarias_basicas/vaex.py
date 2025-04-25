import vaex
import numpy as np
import pandas as pd

# Métodos más utilizados de la biblioteca Vaex:

# 1. vaex.from_arrays():
# Crea un DataFrame a partir de arrays.
df = vaex.from_arrays(nombre=["Ana", "Carlos", "Luis"], edad=[
                      25, 30, 22], ciudad=["Madrid", "Barcelona", "Valencia"])
print("DataFrame creado:")
print(df)

# 2. vaex.from_pandas():
# Convierte un DataFrame de pandas a un DataFrame de Vaex.
pd_df = pd.DataFrame({"nombre": ["Ana", "Carlos", "Luis"], "edad": [
                     25, 30, 22], "ciudad": ["Madrid", "Barcelona", "Valencia"]})
df_vaex = vaex.from_pandas(pd_df)
print("\nDataFrame convertido de Pandas a Vaex:")
print(df_vaex)

# 3. df.head(n):
# Devuelve las primeras n filas del DataFrame.
print("\nPrimeras filas del DataFrame:")
print(df.head(5))

# 4. df.describe():
# Genera estadísticas descriptivas de las columnas numéricas.
print("\nEstadísticas descriptivas:")
print(df.describe())

# 5. df.shape:
# Devuelve las dimensiones del DataFrame (filas, columnas).
print("\nDimensiones del DataFrame:")
print(df.shape)

# 6. df.column_names:
# Devuelve los nombres de las columnas.
print("\nColumnas del DataFrame:")
print(df.column_names)

# 7. df.select("columna"):
# Selecciona una columna específica.
print("\nSeleccionar la columna 'nombre':")
print(df["nombre"])

# 8. df[df["columna"] > valor]:
# Filtra filas que cumplen una condición.
print("\nFiltrar personas mayores de 25 años:")
print(df[df["edad"] > 25])

# 9. df.sort("columna"):
# Ordena el DataFrame por una columna.
print("\nOrdenar por edad de forma ascendente:")
df_sorted = df.sort("edad")
print(df_sorted)

# 10. df.groupby("columna", agg_func):
# Agrupa datos según una columna y aplica una función de agregación.
print("\nContar cuántas personas hay en cada ciudad:")
print(df.groupby("ciudad", agg=vaex.agg.count()))

# 11. df.drop("columna"):
# Elimina una columna del DataFrame.
df_sin_edad = df.drop("edad")
print("\nDataFrame sin la columna 'edad':")
print(df_sin_edad)

# 12. df.mean("columna"):
# Calcula la media de una columna.
print("\nMedia de la edad:")
print(df["edad"].mean())

# 13. df.median("columna"):
# Calcula la mediana de una columna.
print("\nMediana de la edad:")
print(df["edad"].median())

# 14. df.std("columna"):
# Calcula la desviación estándar de una columna.
print("\nDesviación estándar de la edad:")
print(df["edad"].std())

# 15. df.var("columna"):
# Calcula la varianza de una columna.
print("\nVarianza de la edad:")
print(df["edad"].var())

# 16. df.export("archivo.hdf5"):
# Guarda el DataFrame en un archivo HDF5.
df.export("archivo.hdf5")
print("\nDataFrame exportado a HDF5.")

# 17. vaex.open("archivo.hdf5"):
# Carga un archivo HDF5 en un DataFrame de Vaex.
df_cargado = vaex.open("archivo.hdf5")
print("\nDataFrame cargado desde HDF5:")
print(df_cargado.head())

# 18. df.concat(df2):
# Concatena dos DataFrames de Vaex.
df2 = vaex.from_arrays(nombre=["Laura"], edad=[27], ciudad=["Sevilla"])
df_concat = df.concat(df2)
print("\nDataFrame concatenado:")
print(df_concat)

# 19. df.apply():
# Aplica una función personalizada a una columna.
df["edad_doble"] = df["edad"].apply(lambda x: x * 2)
print("\nColumna 'edad_doble' agregada:")
print(df)

# 20. df.unique("columna"):
# Obtiene los valores únicos de una columna.
print("\nValores únicos en la columna 'ciudad':")
print(df["ciudad"].unique())

# 21. df.count():
# Cuenta la cantidad de elementos en cada columna.
print("\nCantidad de elementos en cada columna:")
print(df.count())

# 22. df.mutate(nueva_columna=expresion):
# Crea una nueva columna basada en una expresión.
df = df.mutate(edad_incrementada=df["edad"] + 5)
print("\nNueva columna 'edad_incrementada':")
print(df)

# 23. df.binby("columna", agg=vaex.agg.mean("otra_columna")):
# Realiza binning sobre una columna y calcula la media de otra.
print("\nBinning de edad y media de edad incrementada:")
print(df.binby("edad", agg=vaex.agg.mean("edad_incrementada")))

# 24. df.to_pandas_df():
# Convierte un DataFrame de Vaex a un DataFrame de Pandas.
pd_df = df.to_pandas_df()
print("\nDataFrame convertido a Pandas:")
print(pd_df.head())
