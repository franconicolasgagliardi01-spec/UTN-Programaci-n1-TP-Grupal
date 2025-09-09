"""Ejercicio 6: Multiplicar una Matriz por un Escalar
Escribe un programa que multiplique cada elemento de una lista bidimensional por un
valor escalar dado por el usuario."""

matriz = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

escalar = int(input("Ingrese el valor escalar: "))


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = matriz[i][j] * escalar


print("Matriz resultante:")
for fila in matriz:
    print(fila)