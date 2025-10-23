class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

    def mostrarCeldas(self):
        print(f"Celda({self.fila}, {self.columna}) = {self.valor}")


class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregar_celda(self, fila, columna, valor):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return False
        nueva_celda = Celda(fila, columna, valor)
        self.celdasMatriz.append(nueva_celda)
        return True

    def mostrar_celdas(self):
        print("\nCeldas cargadas:")
        for celda in self.celdasMatriz:
            celda.mostrarCeldas()


def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        print("Debe ingresar un valor ENTERO")


def pedir_valor_entero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.upper() == "FIN":
            return "FIN"
        if entrada.isdigit():
            return entrada
        print("Debe ingresar un valor ENTERO")


def main():
    matriz = Matriz()

    while True:
        valor = pedir_valor_entero("Ingrese el valor para la celda (o 'FIN' para cerrar el programa): ")
        if valor == "FIN":
            break

        fila = pedir_entero("Ingrese la fila (nº entero): ")
        columna = pedir_entero("Ingrese la columna (nº entero): ")

        if matriz.agregar_celda(fila, columna, valor):
            print("Celda agregada correctamente.")
        else:
            print("Ya existe una celda en esa posición. Intente nuevamente")

    matriz.mostrar_celdas()

if __name__ == "__main__":
    main()