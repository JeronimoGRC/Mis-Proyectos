import numpy as np

mi_array = np.array([1,2,3]) # Una dimension
matriz = np.array([[1,2,3],[4,5,6]]) # 2 dimensiones
matriz_con_profundidad = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # 3 dimensiones, es un cubo

#print(mi_array.ndim)
#print(matriz.ndim)
#print(matriz_con_profundidad.ndim)

#Indexar, acceder a una elemento del array
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[1])

#Rangos
print(array1[3:7])

#Indexar para una matriz
print(matriz[1,2])

#Indexar con mas dimensiones
print(matriz_con_profundidad[0,1,2]) # 1º índice Profundidad, 2º índice Fila, 3º indice columna