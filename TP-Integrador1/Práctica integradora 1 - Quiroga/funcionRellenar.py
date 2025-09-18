#Opción (c) - Función para que el técnico rellene golosinas
def rellenarGolosinas(clavesTecnico, golosinas):
    contrasena = input("Ingrese la contraseña: ")
    partes = contrasena.strip().split()
    if partes == list(clavesTecnico):
            codigo = int(input("Ingrese el código de la golosina que desea rellenar: "))
            if 1 <= codigo <= 12:
                cantidad = int(input("Ingrese la cantidad que desea rellenar: "))
                if cantidad > 0:
                    for fila in golosinas:
                        if fila[0] == codigo:
                            fila[2] += cantidad
                            print(f"Se han rellenado {cantidad} unidades de {fila[1]}")
                else:
                    print("La cantidad debe ser mayor a cero")
    else:
            print("No tiene permiso para ejecutar la función de recarga")