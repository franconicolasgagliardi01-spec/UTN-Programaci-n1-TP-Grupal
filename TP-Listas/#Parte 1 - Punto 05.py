cantidad = int(input("Indique la cantidad de números que desea ingresar: "))
multiplicador = int(input("Ingrese el número por el cual desea multiplicar los elementos de la lista: "))
listaNumeros=[]
for i in range(cantidad):
  numero = int(input(f"Ingrese el número {i+1}: "))
  listaNumeros.append(numero)

for i in range(cantidad):
  listaNumeros[i] *= multiplicador
  
print(f"Los valores de la lista multiplicados son: {listaNumeros}")