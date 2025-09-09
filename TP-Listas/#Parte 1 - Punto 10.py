cantidad = int(input("Indique la cantidad de números que desea ingresar: "))
listaNumeros = []
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    listaNumeros.append(numero)

print(f"Los valores de la lista son: {listaNumeros}")

while True:
    eliminarNumero = int(input("Ingrese el índice del valor que desea eliminar de la lista: "))
    if eliminarNumero >= 0 and eliminarNumero < len(listaNumeros):
        del listaNumeros[eliminarNumero]
        break
    else:
        print("El índice ingresado no es válido. Intente nuevamente.")

print(f"Los valores de la lista actualizados son: {listaNumeros}")