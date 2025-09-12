"""Ejercicio 7: Promedio de una Lista
Escribe un programa que permita al usuario ingresar una lista de números y calcule el
promedio de los elementos."""

lista = [] 

salida = False

while salida == False:
    elemento = int(input("Ingrese un elemento a la lista: "))
    lista.append(elemento)
    salir = input("Desea seguir agregando elementos? s/n: ")
    while salir != "s" and salir != "n":
        print("INGRESE UN VALOR VALIDO")
        salir = input("Desea seguir agregando elementos? s/n: ")
    if salir == "n":
        salida = True
    else:
        pass

longitud= len(lista)

suma = sum(lista)

promedio = suma / longitud

print(f"El promedio de nota del estudiante es: {promedio}")