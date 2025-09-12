"""Explique y ejemplifique la libreria NUMPY para trabajar con matrices y arrays"""

#NumPy es una biblioteca de Python de código abierto para la computación numérica, especialmente conocida por su estructura de datos principal, el array multidimensional (ndarray), que permite manejar y realizar operaciones matemáticas eficientes en grandes volúmenes de datos. 

import numpy as np

# Crear un arreglo con 3 números
lista = np.array([1, 2, 3])

print(lista)

print("-------------------------")
#Crea una matriz bidimensional de 2x2
ones = np.ones((2,2))
print(ones)
print("-------------------------")
#Saca el promedio de una lista
valores = np.array([10, 20, 30, 40])

promedio = np.mean(valores)

print(promedio)



