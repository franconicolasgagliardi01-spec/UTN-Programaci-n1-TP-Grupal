#Opción (d) - Función para mostrar golosinas pedidas y apagar la máquina
def apagarMaquina(golosinasPedidas):
    global salida
    salida = True
    print("Golosinas pedidas: \n", golosinasPedidas[1], "\nCantidad: ", golosinasPedidas[2])
    print("Apagando máquina...")