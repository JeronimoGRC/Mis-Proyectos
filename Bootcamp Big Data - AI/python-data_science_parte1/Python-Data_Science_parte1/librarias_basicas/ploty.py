import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Métodos más utilizados de la biblioteca plotly:

# 1. px.line():
# Crea un gráfico de líneas.
df = pd.DataFrame({"x": np.linspace(0, 10, 100),
                  "y": np.sin(np.linspace(0, 10, 100))})
fig = px.line(df, x="x", y="y", title="Gráfico de Líneas con Plotly")
fig.show()

# 2. px.scatter():
# Crea un gráfico de dispersión.
df = pd.DataFrame({"x": np.random.rand(50), "y": np.random.rand(
    50), "categoria": np.random.choice(["A", "B"], 50)})
fig = px.scatter(df, x="x", y="y", color="categoria",
                 title="Gráfico de Dispersión con Categorías")
fig.show()

# 3. px.bar():
# Crea un gráfico de barras.
df = pd.DataFrame(
    {"categorias": ["A", "B", "C", "D"], "valores": [5, 7, 3, 8]})
fig = px.bar(df, x="categorias", y="valores",
             title="Gráfico de Barras con Plotly")
fig.show()

# 4. px.histogram():
# Crea un histograma.
datos = np.random.randn(1000)
df = pd.DataFrame({"valores": datos})
fig = px.histogram(df, x="valores", nbins=30, title="Histograma con Plotly")
fig.show()

# 5. px.box():
# Crea un diagrama de caja.
df = pd.DataFrame({"categoria": np.random.choice(
    ["A", "B", "C"], 100), "valor": np.random.randn(100)})
fig = px.box(df, x="categoria", y="valor", title="Diagrama de Caja con Plotly")
fig.show()

# 6. px.violin():
# Crea un gráfico de violín.
fig = px.violin(df, x="categoria", y="valor", box=True,
                points="all", title="Gráfico de Violín con Plotly")
fig.show()

# 7. px.pie():
# Crea un gráfico de pastel.
df = pd.DataFrame({"categorias": ["A", "B", "C"], "valores": [20, 30, 50]})
fig = px.pie(df, names="categorias", values="valores",
             title="Gráfico de Pastel con Plotly")
fig.show()

# 8. px.funnel():
# Crea un gráfico de embudo.
df = pd.DataFrame({"etapa": ["Visitantes", "Registrados",
                  "Compradores"], "cantidad": [1000, 600, 200]})
fig = px.funnel(df, x="cantidad", y="etapa",
                title="Gráfico de Embudo con Plotly")
fig.show()

# 9. px.treemap():
# Crea un gráfico de árbol.
df = pd.DataFrame({"categoria": ["A", "A", "B", "B", "C"], "subcategoria": [
                  "A1", "A2", "B1", "B2", "C1"], "valor": [100, 200, 150, 250, 300]})
fig = px.treemap(df, path=["categoria", "subcategoria"],
                 values="valor", title="Gráfico de Árbol con Plotly")
fig.show()

# 10. px.sunburst():
# Crea un gráfico de sol radial.
fig = px.sunburst(df, path=["categoria", "subcategoria"],
                  values="valor", title="Gráfico de Sol Radial con Plotly")
fig.show()

# 11. px.scatter_3d():
# Crea un gráfico de dispersión en 3D.
df = pd.DataFrame({"x": np.random.rand(
    50), "y": np.random.rand(50), "z": np.random.rand(50)})
fig = px.scatter_3d(df, x="x", y="y", z="z",
                    title="Gráfico de Dispersión 3D con Plotly")
fig.show()

# 12. px.line_3d():
# Crea un gráfico de líneas en 3D.
fig = px.line_3d(df, x="x", y="y", z="z",
                 title="Gráfico de Líneas 3D con Plotly")
fig.show()

# 13. px.parallel_coordinates():
# Crea un gráfico de coordenadas paralelas.
df = px.data.iris()
fig = px.parallel_coordinates(df, dimensions=[
                              "sepal_width", "sepal_length", "petal_width", "petal_length"], color="species_id")
fig.show()

# 14. px.density_contour():
# Crea un gráfico de contorno de densidad.
fig = px.density_contour(df, x="sepal_length", y="sepal_width",
                         title="Gráfico de Contorno de Densidad con Plotly")
fig.show()

# 15. px.density_heatmap():
# Crea un gráfico de mapa de calor de densidad.
fig = px.density_heatmap(df, x="sepal_length", y="sepal_width",
                         title="Mapa de Calor de Densidad con Plotly")
fig.show()

# 16. go.Figure():
# Crea gráficos personalizados con múltiples trazas.
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df.index, y=df["sepal_length"], mode="lines", name="Serie 1"))
fig.add_trace(go.Scatter(
    x=df.index, y=df["sepal_width"], mode="lines+markers", name="Serie 2"))
fig.update_layout(title="Gráfico Personalizado con Plotly")
fig.show()
