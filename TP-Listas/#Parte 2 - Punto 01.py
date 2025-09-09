
def generar_matriz(filas, columnas):
    matriz = []
    contador = 1
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(contador)
            contador += 1
        matriz.append(fila)
    return matriz

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = generar_matriz(filas, columnas)
for fila in matriz:
    print(fila)