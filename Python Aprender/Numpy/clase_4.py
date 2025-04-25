import numpy as np
#Concatenar arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arrFinal = np.concatenate((arr1, arr2)) #Caso por defecto axis=0

#print(arrFinal)

#Concatenar matrices
matr1 = np.array([[1,2],[3,4]])
matr2 = np.array([[5,6],[7,8]])

matrFinal = np.concatenate((matr1, matr2),axis=1)
#axis=0 [[1 2] -> 4 Filas 2 columnas
#        [3 4]
#        [5 6]
#        [7 8]]

#axis=1 -> 2 filas 4 columnas
# [[1 2 5 6]
# [3 4 7 8]]
print(matrFinal)

#Separar arrays
newarr = np.array_split(matrFinal,3) # Dividimos la matriz en 3 arrays
print(newarr) 
#[array([[1, 2, 5, 6]]), array([[3, 4, 7, 8]]), array([], shape=(0, 4), dtype=int32)] 
#El último elemento del array al querer dividirlo en 3 estará vacío

newarr2 = np.array_split(arrFinal,4)
print(newarr2) 
#[array([1, 2]), array([3, 4]), array([5]), array([6])]
#Numpy reparte el resto de elementos del array para hacer arrays de solo un elemento

x = np.where(arrFinal == 4)
print(x)

arr = np.array([3,2,0,1])
array_sort = np.sort(arr) 
print(array_sort)