"""Ejercicio 7: Promedio de una Lista
Escribe un programa que permita al usuario ingresar una lista de números y calcule el
promedio de los elementos."""

lista = [0] * 5

for i in range(0,5):
    lista[i] = int(input(f"Ingrese un numero en la posicion {i}, de la lista "))


suma = sum(lista)

promedio = suma / 5

print(f"El promedio de nota del estudiante es: {promedio}")