import numpy as np

# Métodos más utilizados de la biblioteca numpy:

# 1. np.array():
# Crea un array de NumPy a partir de una lista o tupla.
arr = np.array([1, 2, 3, 4, 5])
print("Array creado:")
print(arr)

# 2. np.zeros((filas, columnas)):
# Crea un array de ceros con la forma especificada.
ceros = np.zeros((3, 3))
print("\nArray de ceros:")
print(ceros)

# 3. np.ones((filas, columnas)):
# Crea un array de unos con la forma especificada.
unos = np.ones((2, 4))
print("\nArray de unos:")
print(unos)

# 4. np.eye(n):
# Crea una matriz identidad de tamaño n x n.
identidad = np.eye(4)
print("\nMatriz identidad:")
print(identidad)

# 5. np.arange(inicio, fin, paso):
# Genera un array con valores dentro de un rango con un paso determinado.
rango = np.arange(0, 10, 2)
print("\nArray con rango especificado:")
print(rango)

# 6. np.linspace(inicio, fin, num):
# Genera un array con 'num' elementos equiespaciados entre inicio y fin.
espaciado = np.linspace(0, 1, 5)
print("\nArray con valores equiespaciados:")
print(espaciado)

# 7. np.random.rand(filas, columnas):
# Genera un array de números aleatorios entre 0 y 1.
aleatorio = np.random.rand(3, 3)
print("\nArray aleatorio entre 0 y 1:")
print(aleatorio)

# 8. np.random.randint(inicio, fin, tamaño):
# Genera un array de enteros aleatorios en un rango especificado.
ent_aleatorio = np.random.randint(1, 100, (2, 2))
print("\nArray de enteros aleatorios:")
print(ent_aleatorio)

# 9. np.shape(arr):
# Devuelve la forma del array (filas, columnas).
print("\nForma del array:")
print(arr.shape)

# 10. np.size(arr):
# Devuelve el número total de elementos en el array.
print("\nNúmero total de elementos en el array:")
print(arr.size)

# 11. np.reshape(arr, (filas, columnas)):
# Cambia la forma del array sin alterar sus datos.
arr_reshaped = arr.reshape((5, 1))
print("\nArray reestructurado:")
print(arr_reshaped)

# 12. np.transpose(arr):
# Transpone una matriz (intercambia filas y columnas).
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatriz original:")
print(matriz)
print("\nMatriz transpuesta:")
print(np.transpose(matriz))

# 13. np.max(arr):
# Devuelve el valor máximo en el array.
print("\nValor máximo en el array:")
print(np.max(arr))

# 14. np.min(arr):
# Devuelve el valor mínimo en el array.
print("\nValor mínimo en el array:")
print(np.min(arr))

# 15. np.mean(arr):
# Devuelve la media de los valores en el array.
print("\nMedia del array:")
print(np.mean(arr))

# 16. np.median(arr):
# Devuelve la mediana de los valores en el array.
print("\nMediana del array:")
print(np.median(arr))

# 17. np.std(arr):
# Devuelve la desviación estándar del array.
print("\nDesviación estándar del array:")
print(np.std(arr))

# 18. np.var(arr):
# Devuelve la varianza del array.
print("\nVarianza del array:")
print(np.var(arr))

# 19. np.sqrt(arr):
# Devuelve la raíz cuadrada de cada elemento del array.
print("\nRaíz cuadrada de los elementos del array:")
print(np.sqrt(arr))

# 20. np.sum(arr):
# Devuelve la suma de todos los elementos en el array.
print("\nSuma de los elementos del array:")
print(np.sum(arr))

# 21. np.prod(arr):
# Devuelve el producto de todos los elementos del array.
print("\nProducto de los elementos del array:")
print(np.prod(arr))

# 22. np.dot(arr1, arr2):
# Calcula el producto punto de dos arrays.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\nProducto punto de dos arrays:")
print(np.dot(arr1, arr2))

# 23. np.linalg.inv(matriz):
# Calcula la matriz inversa (requiere matriz cuadrada).
matriz_cuadrada = np.array([[2, 3], [1, 4]])
print("\nMatriz inversa:")
print(np.linalg.inv(matriz_cuadrada))

# 24. np.linalg.det(matriz):
# Calcula el determinante de una matriz.
print("\nDeterminante de la matriz:")
print(np.linalg.det(matriz_cuadrada))

# 25. np.linalg.eig(matriz):
# Calcula los valores y vectores propios de una matriz cuadrada.
valores_propios, vectores_propios = np.linalg.eig(matriz_cuadrada)
print("\nValores propios de la matriz:")
print(valores_propios)
print("\nVectores propios de la matriz:")
print(vectores_propios)

print(arr1 * arr2)