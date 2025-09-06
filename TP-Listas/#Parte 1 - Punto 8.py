#Parte 1 - Punto 8
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

tamaño = len(lista)
lista_confirmar = []
elementos_repetidos = []

for i in range(0,tamaño):
    if lista[i] in lista_confirmar:
        elementos_repetidos.append(lista[i])
    else:
        lista_confirmar.append(lista[i])

print(f"Elementos repetidos dentro de la lista: {elementos_repetidos}")