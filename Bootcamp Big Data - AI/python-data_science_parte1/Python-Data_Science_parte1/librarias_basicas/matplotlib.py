import matplotlib.pyplot as plt
import numpy as np

# Métodos más utilizados de la biblioteca matplotlib:

# 1. plt.plot(x, y):
# Crea un gráfico de líneas con los valores proporcionados.
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='Seno')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Seno')
plt.legend()
plt.show()

# 2. plt.scatter(x, y):
# Crea un gráfico de dispersión con los valores proporcionados.
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color='red', label='Puntos')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Dispersión')
plt.legend()
plt.show()

# 3. plt.bar(x, y):
# Crea un gráfico de barras.
categorias = ['A', 'B', 'C', 'D']
valores = [5, 7, 3, 8]
plt.bar(categorias, valores, color='blue')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')
plt.show()

# 4. plt.hist(datos, bins):
# Crea un histograma de los datos proporcionados.
datos = np.random.randn(1000)
plt.hist(datos, bins=30, color='green', alpha=0.7)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma')
plt.show()

# 5. plt.pie(valores, labels, autopct):
# Crea un gráfico de pastel con los valores proporcionados.
valores = [20, 30, 50, 22]
labels = ['A', 'B', 'C','D']
plt.pie(valores, labels=labels, autopct='%1.1f%%',
        colors=['red', 'blue', 'green','orange'])
plt.title('Gráfico de Pastel')
plt.show()

# 6. plt.subplot(nrows, ncols, index):
# Crea múltiples subgráficos en una sola figura.
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title("Seno")
axs[0, 1].scatter(x, y, color='red')
axs[0, 1].set_title("Dispersión")
axs[1, 0].bar(categorias, valores, color='blue')
axs[1, 0].set_title("Barras")
axs[1, 1].hist(datos, bins=30, color='green', alpha=0.7)
axs[1, 1].set_title("Histograma")
plt.tight_layout()
plt.show()

# 7. plt.boxplot(datos):
# Crea un diagrama de caja para visualizar la distribución de los datos.
plt.boxplot(datos)
plt.title("Diagrama de Caja")
plt.show()

# 8. plt.violinplot(datos):
# Crea un gráfico de violín para visualizar la distribución de los datos.
plt.violinplot(datos)
plt.title("Gráfico de Violín")
plt.show()

# 9. plt.errorbar(x, y, yerr=0.1):
# Crea un gráfico de líneas con barras de error.
y_err = 0.1 * np.ones_like(y)
plt.errorbar(x, y, yerr=y_err, fmt='-o')
plt.title("Gráfico con Barras de Error")
plt.show()

# 10. plt.stem(x, y):
# Crea un gráfico de líneas con marcadores verticales.
plt.stem(x, y)
plt.title("Gráfico de Tallos")
plt.show()

# 11. plt.hexbin(x, y, gridsize=25, cmap='Blues'):
# Crea un gráfico de densidad hexagonal.
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.hexbin(x, y, gridsize=25, cmap='Blues')
plt.colorbar(label='Frecuencia')
plt.title("Gráfico de Densidad Hexagonal")
plt.show()

# 12. plt.contour(X, Y, Z):
# Crea un gráfico de contorno para visualizar funciones en 2D.
X, Y = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))
Z = np.sin(X**2 + Y**2)
plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar()
plt.title("Gráfico de Contorno")
plt.show()

# 13. plt.streamplot(X, Y, U, V):
# Crea un gráfico de líneas de flujo para representar campos vectoriales.
U, V = np.cos(X), np.sin(Y)
plt.streamplot(X, Y, U, V, color='blue')
plt.title("Gráfico de Líneas de Flujo")
plt.show()

# 14. plt.imshow(Z, cmap='hot'):
# Muestra una imagen a partir de una matriz de valores.
plt.imshow(Z, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("Mapa de Calor")
plt.show()

# 15. plt.loglog(x, y):
# Crea un gráfico de líneas en escala log-log.
plt.loglog(x, y)
plt.title("Gráfico Log-Log")
plt.show()
