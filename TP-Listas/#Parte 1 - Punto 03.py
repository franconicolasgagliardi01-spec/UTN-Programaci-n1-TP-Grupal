#Parte 1 - Punto 3
lista = []
salida = False

while salida == False:
    elemento = input("Ingrese un elemento a la lista: ")
    lista.append(elemento)
    salir = input("Desea seguir agregando elementos? s/n: ")
    while salir != "s" and salir != "n":
        print("INGRESE UN VALOR VALIDO")
        salir = input("Desea seguir agregando elementos? s/n: ")
    if salir == "n":
        salida = True
    else:
        pass

print(f"Lista normal: {lista}")
lista.reverse()
print(f"Lista al reves: {lista}")