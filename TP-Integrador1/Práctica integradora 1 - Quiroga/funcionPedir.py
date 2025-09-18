#Opción (a) - Función para pedir golosinas
def pedirGolosinas(golosinas, empleados, golosinasPedidas):
    legajo = int(input("Ingrese su legajo: "))
    if legajo in empleados:
        codigo = int(input("Ingrese el código de la golosina que desea:\n 1- KitKat\n 2- Chicles\n 3- Caramelos de menta\n 4- Huevo Kinder\n 5- Chetoo\n 6- Twix\n 7- M&M'S\n 8- Papas Lay\n 9- Milkybar\n 10- Alfajor Tofi\n 11- Lata Coca\n 12- Chitos\n"))
        if 1 <= codigo <= 12:
            cantidad = int(input("Ingrese la cantidad que desea: "))
            if cantidad > 0:
                for fila in golosinas:
                    if fila[0] == codigo:
                        if fila[2] >= cantidad:
                            fila[2] -= cantidad
                            golosinasPedidas[0] = fila[0]
                            golosinasPedidas[1] = fila[1]
                            golosinasPedidas[2] = cantidad
                            print(f"Se han entregado {cantidad} unidades de {fila[1]}.")
                        else:
                            print(f"Lo sentimos, la golosina {fila[1]} no se encuentra disponible, seleccione otra golosina o ingrese 'd' si desea apagar la máquina.")
            else:
                print("La cantidad debe ser mayor a cero")
        else:
            print("Código de golosina inválido")
    else:
        print("Usted no es un empleado de la empresa")