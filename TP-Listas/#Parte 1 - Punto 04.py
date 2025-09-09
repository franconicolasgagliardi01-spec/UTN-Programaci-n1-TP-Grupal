"""Ejercicio 4: Contar Elementos Pares e Impares
Escribe un programa que pida al usuario una lista de números y cuente cuántos de
ellos son pares y cuántos son impares."""

lista = [0] * 10

pares = 0

impares = 0

for i in range(0,10):
    lista[i] = int(input(f"Ingrese un numero en la posicion {i}, de la lista "))

for i in range (0,10):
    if lista[i] % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"La cantidad de numeros pares de la lista es: {pares}")

print(f"La cantidad de numeros impares de la lista es: {impares}")