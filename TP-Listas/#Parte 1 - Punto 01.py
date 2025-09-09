"""Ejercicio 1: Suma de Elementos
Escribe un programa que permita al usuario ingresar una lista de números y calcule la
suma de todos los elementos en la lista."""

lista = [0] * 10

for i in range(0,10):
    lista[i] = int(input(f"Ingrese un numero en la posicion {i}, de la lista "))


suma = sum(lista)

print(f"La suma de todos los valores de la lista entre si da como resultado: {suma}")

