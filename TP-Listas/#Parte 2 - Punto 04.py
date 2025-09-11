"""Ejercicio 4: Matriz Transpuesta
Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una
matriz intercambia sus filas por columnas."""

matriz = [[1, 2, 3],[4, 5, 6]]


print("Matriz original:")
for fila in matriz:
    print(fila)


transpuesta = []
for j in range(len(matriz[0])):  
    nueva_fila = []
    for i in range(len(matriz)):  
        nueva_fila.append(matriz[i][j])
    transpuesta.append(nueva_fila)


print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)