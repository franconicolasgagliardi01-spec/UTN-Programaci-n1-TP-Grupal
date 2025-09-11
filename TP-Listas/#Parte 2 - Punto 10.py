"""Ejercicio 10: Verificar Matriz Simétrica
Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique
si una matriz es simétrica."""

n = int(input("¿De qué tamaño es la matriz cuadrada? (Ej: 3 para 3x3): "))

print("Ingresa los números fila por fila (separados por espacio):")
matriz = [[int(x) for x in input(f"Fila {i+1}: ").split()] for i in range(n)]

simetrica = True
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if simetrica:
    print("La matriz es simétrica.")
else:
    print("La matriz NO es simétrica.")