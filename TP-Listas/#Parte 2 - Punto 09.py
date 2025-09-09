"""Ejercicio 9: Matriz Identidad Inversa
Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz
identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa
principal son 1 y el resto son 0."""

n = 4
Identidadinversa = [[1 if i + j == n - 1 else 0 for j in range(n)] for i in range(n)]
for fila in Identidadinversa:
    print(fila)