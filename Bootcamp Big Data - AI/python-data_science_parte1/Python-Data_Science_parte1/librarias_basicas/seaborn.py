import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Métodos más utilizados de la biblioteca seaborn:

# 1. sns.lineplot(x, y, data):
# Crea un gráfico de líneas con los valores proporcionados.
df = pd.DataFrame({"x": np.linspace(0, 10, 100),
                  "y": np.sin(np.linspace(0, 10, 100))})
sns.lineplot(x="x", y="y", data=df)
plt.title("Gráfico de Líneas con Seaborn")
plt.show()

# 2. sns.scatterplot(x, y, data, hue):
# Crea un gráfico de dispersión con colores por categoría.
df = pd.DataFrame({"x": np.random.rand(50), "y": np.random.rand(
    50), "categoria": np.random.choice(["A", "B"], 50)})
sns.scatterplot(x="x", y="y", hue="categoria", data=df)
plt.title("Gráfico de Dispersión con Categorías")
plt.show()

# 3. sns.barplot(x, y, data):
# Crea un gráfico de barras con agregaciones.
df = pd.DataFrame(
    {"categorias": ["A", "B", "C", "D"], "valores": [5, 7, 3, 8]})
sns.barplot(x="categorias", y="valores", data=df)
plt.title("Gráfico de Barras con Seaborn")
plt.show()

# 4. sns.histplot(datos, bins):
# Crea un histograma de los datos proporcionados.
datos = np.random.randn(1000)
sns.histplot(datos, bins=30, kde=True)
plt.title("Histograma con Seaborn")
plt.show()

# 5. sns.boxplot(x, y, data):
# Crea un diagrama de caja para visualizar la distribución de los datos.
df = pd.DataFrame({"categoria": np.random.choice(
    ["A", "B", "C"], 100), "valor": np.random.randn(100)})
sns.boxplot(x="categoria", y="valor", data=df)
plt.title("Diagrama de Caja con Seaborn")
plt.show()

# 6. sns.violinplot(x, y, data):
# Crea un gráfico de violín para visualizar la distribución de los datos.
sns.violinplot(x="categoria", y="valor", data=df)
plt.title("Gráfico de Violín con Seaborn")
plt.show()

# 7. sns.heatmap(data, annot=True, cmap):
# Crea un mapa de calor a partir de una matriz de valores.
data = np.random.rand(10, 10)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Mapa de Calor con Seaborn")
plt.show()

# 8. sns.pairplot(data):
# Crea gráficos de dispersión para todas las combinaciones de variables numéricas.
df_species = sns.load_dataset("iris")


sns.pairplot(df_species, hue="species")
plt.show()


df_categoria = pd.DataFrame({"categoria": np.random.choice(
    ["A", "B", "C"], 100), "valor": np.random.randn(100)})
sns.boxplot(x="categoria", y="valor", data=df_categoria)
plt.title("Diagrama de Caja con Seaborn")
plt.show()

# 9. sns.regplot(x, y, data):
# Crea un gráfico de dispersión con una línea de regresión.
df = pd.DataFrame({
    "x": np.linspace(0, 10, 50),
    "y": 2 * np.linspace(0, 10, 50) + np.random.randn(50)  # Relación lineal con ruido
})
sns.regplot(x="x", y="y", data=df)
plt.title("Gráfico de Regresión con Seaborn")
plt.show()


# 10. sns.countplot(x, data):
# Cuenta la frecuencia de cada categoría en una columna y la representa en un gráfico de barras.


sns.countplot(x="categoria", data=df_categoria)
plt.title("Gráfico de Frecuencia con Seaborn")
plt.show()


# 11. sns.lmplot(x, y, data, hue):
# Crea un gráfico de regresión con diferentes categorías.
sns.lmplot(x="sepal_length", y="sepal_width", hue="species", data=df_species)
plt.show()


# 12. sns.jointplot(x, y, data, kind):
# Crea un gráfico conjunto combinando dispersión y histogramas.
sns.jointplot(x="sepal_length", y="sepal_width", data=df_species, kind="scatter")
plt.show()


# 13. sns.swarmplot(x, y, data):
# Muestra la distribución de los datos con puntos desplazados.
sns.swarmplot(x="categoria", y="valor", data=df_categoria)
plt.title("Swarm Plot con Seaborn")
plt.show()


# 14. sns.ecdfplot(x, data):
# Muestra la función de distribución acumulativa de los datos.
sns.ecdfplot(x="sepal_length", data=df_species)
plt.show()


# 15. sns.kdeplot(x, data, fill=True):
# Crea una estimación de la densidad del núcleo.
sns.kdeplot(x="sepal_length", data=df_species, fill=True)
plt.show()


# 16. sns.clustermap(data, cmap):
# Muestra un mapa de calor jerárquico.
sns.clustermap(df.corr(), cmap="coolwarm", annot=True)
plt.show()


# 17. sns.boxenplot(x, y, data):
# Muestra un gráfico de caja mejorado para grandes conjuntos de datos.
sns.boxenplot(x="categoria", y="valor", data=df_categoria)
plt.show()


# 18. sns.residplot(x, y, data):
# Muestra los residuos de un ajuste de regresión.
sns.residplot(x="sepal_length", y="sepal_width", data=df_species)
plt.show()


# 19. sns.pointplot(x, y, data):
# Muestra las medias de diferentes categorías con intervalos de confianza.
sns.pointplot(x="categoria", y="valor", data=df_categoria)
plt.show()


# 20. sns.despine():
# Elimina los bordes superiores y derechos de un gráfico.
sns.histplot(datos, bins=30)
sns.despine()
plt.show()