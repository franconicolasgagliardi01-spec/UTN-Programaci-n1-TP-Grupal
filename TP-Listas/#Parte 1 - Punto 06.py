"""Ejercicio 6: Eliminar Duplicados
Escribe un programa que permita al usuario ingresar una lista de números y elimine los
elementos duplicados.
Pista:
 Utiliza la función set()."""

entrada = input("Ingresa números separados por comas(sin espacios): ")

numeros = entrada.split(",")
numeros_sin_duplicados = list(set(numeros))

print("Sin duplicados:", numeros_sin_duplicados)