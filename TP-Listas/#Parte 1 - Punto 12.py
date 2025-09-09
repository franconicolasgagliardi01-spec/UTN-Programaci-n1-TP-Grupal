"""Ejercicio 12: Sumar Listas Elemento por Elemento
Escribe un programa que sume dos listas de números elemento por elemento. Las
listas deben tener la misma longitud."""

lista = [0] * 5

lista2 = [0] * 5

lista3 = [0] * 5

for i in range(0,5):

    lista[i] = int(input(f"Ingrese un numero en la posicion {i}, de la lista "))

    lista2[i] = int(input(f"Ingrese un numero en la posicion {i}, de la lista 2 "))

    lista3[i] = [lista[i]+lista2[i]]


print(lista3)