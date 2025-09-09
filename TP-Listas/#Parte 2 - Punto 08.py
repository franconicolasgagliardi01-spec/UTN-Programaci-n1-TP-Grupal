
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

identidad = [[1 if i == j else 0 for j in range(columnas)] for i in range(filas)]
for fila in identidad:
    print(fila)