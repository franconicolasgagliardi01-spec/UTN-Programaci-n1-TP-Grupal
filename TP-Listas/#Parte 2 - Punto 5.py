
def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingresa el valor para la posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = generar_matriz(filas, columnas)
for fila in matriz:
    print(fila)
print("El valor más grande en la matriz es:", max(max(fila) for fila in matriz))