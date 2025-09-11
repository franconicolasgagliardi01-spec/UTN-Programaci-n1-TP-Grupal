"""Ejercicio 9: Lista de Números Primos
Escribe un programa que permita al usuario ingresar una lista de números y filtre los
números primos.
Pista:
 Usa una función para verificar si un número es primo"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):  
        if n % i == 0:    
            return False
    return True            

numeros = input("Ingresá números separados por espacios: ")
lista = [int(x) for x in numeros.split()]


primos = []
for n in lista:
    if es_primo(n):
        primos.append(n)

print("Números primos en la lista:", primos)