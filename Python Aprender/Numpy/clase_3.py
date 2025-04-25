import numpy as np

mi_array = np.array([1,2,3,4])
mi_matriz = np.array([[1,2,3,4],[5,6,7,8]])
matriz_con_profundidad = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # 3 dimensiones, es un cubo
#Para saber la forma

#print(np.shape(mi_array)) #Devuelve (4,) -> Un array de una dimensión de 4 elementos
#print(np.shape(mi_matriz)) #Devuelve (2, 4) -> Un array de 2 dimensiones de 4 elementos

#Re shape -> Cambia el tamaño del array
mi_matriz = mi_matriz.reshape(4,2) 
#print(mi_matriz)

# Iterar un array numpy
i = 0
for matriz in matriz_con_profundidad:
    print(f"Matriz {i}-> {matriz}")
    i += 1
    
for matriz in matriz_con_profundidad:
    for fila in matriz:   
        print(f"Fila {i}-> {fila}")
        i += 1

for matriz in matriz_con_profundidad:
    for fila in matriz:   
        for elemento in fila:
            print(f"Elemento {i}-> {elemento}")
            i += 1