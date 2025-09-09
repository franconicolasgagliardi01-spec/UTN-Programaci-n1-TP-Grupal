#Escribe un programa que pida al usuario una lista de números y encuentre el mayor y el menor de ellos.
cantidad = int(input("Indique la cantidad de números que desea ingresar: "))
listaNumeros=[]
for i in range(cantidad):
  numero = int(input(f"Ingrese el número {i+1}: "))
  listaNumeros.append(numero)

mayor = print(f"El mayor número de la lista es: {max(listaNumeros)}")
menor = print(f"El menor número de la lista es: {min(listaNumeros)}")