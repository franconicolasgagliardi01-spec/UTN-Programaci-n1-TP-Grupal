"""Ejercicio 7: Diagonal de una Matriz Cuadrada
Escribe un programa que extraiga los elementos de la diagonal principal de una matriz
cuadrada.
"""

n = int(input("¿De qué tamaño es la matriz cuadrada? (Ej: 3 para 3x3): "))

print("Ahora ingresa los números fila por fila (separados por espacio).")
matriz = [[int(x) for x in input(f"Fila {i+1}: ").split()] for i in range(n)]

print("Matriz completa:")
for fila in matriz:
    print(fila)

diagonal = [matriz[i][i] for i in range(n)]

print("Diagonal principal:")
print(diagonal)