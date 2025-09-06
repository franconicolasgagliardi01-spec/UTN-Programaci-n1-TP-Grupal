#Parte 1 - Punto 11
lista = [] 
salida = False

while salida == False:
    elemento = float(input("Ingrese un numero a la lista: "))
    lista.append(elemento)
    salir = input("Desea seguir agregando numeros? s/n: ")
    while salir != "s" and salir != "n":
        print("INGRESE UN VALOR VALIDO")
        salir = input("Desea seguir agregando numeros? s/n: ")
    if salir == "n":
        salida = True
    else:
        pass

numero = float(input("Ingrese un numero para buscar en la lista: "))
contador = 0

for num in lista:
    if num == numero:
        contador += 1

if contador == 1:
    print(f"El numero ingresado aparece {contador} vez en la lista")
else:
    print(f"El numero ingresado aparece {contador} veces en la lista")
