import dask.dataframe as dd
import dask.array as da
import dask.bag as db
from dask.diagnostics import ProgressBar
import numpy as np
import pandas as pd

# Métodos más utilizados de la biblioteca Dask:

# 1. dd.read_csv():
# Carga un archivo CSV en un DataFrame de Dask.
df = dd.read_csv("archivo.csv")
print("DataFrame cargado desde CSV con Dask.")

# 2. dd.from_pandas():
# Convierte un DataFrame de Pandas en un DataFrame de Dask.
pd_df = pd.DataFrame({"A": range(10), "B": range(10, 20)})
ddf = dd.from_pandas(pd_df, npartitions=2)
print("DataFrame convertido de Pandas a Dask.")

# 3. ddf.head():
# Muestra las primeras filas del DataFrame.
print("\nPrimeras filas del DataFrame:")
print(ddf.head())

# 4. ddf.compute():
# Convierte un DataFrame de Dask en un DataFrame de Pandas.
pd_result = ddf.compute()
print("\nDataFrame de Dask convertido a Pandas:")
print(pd_result)

# 5. ddf.describe():
# Calcula estadísticas descriptivas de un DataFrame.
print("\nEstadísticas descriptivas del DataFrame:")
print(ddf.describe().compute())

# 6. ddf.groupby():
# Agrupa datos por una columna y calcula una métrica.
ddf_grouped = ddf.groupby("A").sum()
print("\nDatos agrupados y sumados:")
print(ddf_grouped.compute())

# 7. ddf.merge():
# Realiza una fusión (join) de DataFrames.
df2 = dd.from_pandas(pd.DataFrame(
    {"A": range(5), "C": range(50, 55)}), npartitions=2)
ddf_merged = ddf.merge(df2, on="A", how="left")
print("\nDataFrame fusionado:")
print(ddf_merged.compute())

# 8. ddf.drop():
# Elimina una columna del DataFrame.
ddf_dropped = ddf.drop(columns=["B"])
print("\nDataFrame después de eliminar la columna B:")
print(ddf_dropped.compute())

# 9. ddf.fillna():
# Rellena valores nulos en un DataFrame.
ddf_filled = ddf.fillna(0)
print("\nDataFrame con valores nulos reemplazados:")
print(ddf_filled.compute())

# 10. ddf.nunique():
# Cuenta los valores únicos en cada columna.
print("\nNúmero de valores únicos en cada columna:")
print(ddf.nunique().compute())

# 11. da.arange():
# Crea un array distribuido de Dask.
arr = da.arange(100, chunks=10)
print("\nArray distribuido creado con Dask:")
print(arr)

# 12. da.mean():
# Calcula la media de un array distribuido.
print("\nMedia del array distribuido:")
print(arr.mean().compute())

# 13. da.std():
# Calcula la desviación estándar de un array distribuido.
print("\nDesviación estándar del array distribuido:")
print(arr.std().compute())

# 14. da.max():
# Encuentra el valor máximo en un array distribuido.
print("\nValor máximo en el array distribuido:")
print(arr.max().compute())

# 15. da.min():
# Encuentra el valor mínimo en un array distribuido.
print("\nValor mínimo en el array distribuido:")
print(arr.min().compute())

# 16. da.dot():
# Producto punto entre arrays de Dask.
a = da.random.random((1000, 1000), chunks=(100, 100))
b = da.random.random((1000, 1000), chunks=(100, 100))
dot_product = da.dot(a, b)
print("\nProducto punto calculado:")
print(dot_product.compute())

# 17. da.linalg.svd():
# Calcula la descomposición en valores singulares (SVD).
U, S, V = da.linalg.svd(a)
print("\nSVD calculado:")
print(S.compute())

# 18. da.cov():
# Calcula la matriz de covarianza de un array distribuido.
print("\nMatriz de covarianza del array distribuido:")
print(da.cov(a).compute())

# 19. db.from_sequence():
# Crea un Bag de Dask a partir de una secuencia.
bag = db.from_sequence([1, 2, 3, 4, 5])
print("\nBag de Dask creado:")
print(bag)

# 20. bag.distinct():
# Obtiene valores únicos en un Bag de Dask.
print("\nValores únicos en el Bag:")
print(bag.distinct().compute())

# 21. ProgressBar():
# Muestra una barra de progreso en operaciones de Dask.
with ProgressBar():
    result = ddf.sum().compute()
print("\nResultado con barra de progreso:")
print(result)

# 22. ddf.to_parquet():
# Guarda un DataFrame de Dask en formato Parquet.
ddf.to_parquet("output_parquet", engine="pyarrow")
print("\nDataFrame guardado en formato Parquet.")
