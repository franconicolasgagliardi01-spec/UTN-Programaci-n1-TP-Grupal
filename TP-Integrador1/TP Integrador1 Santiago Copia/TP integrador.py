
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10],
]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

clavesTecnico = ("admin", "13221", "2025")

golosinasPedidas = []


def pedir_golosina():
    legajo = int(input("Ingrese su legajo: "))
    if legajo not in empleados:
        print("Usted no es un empleado de la empresa")
        return

    while True:
        codigo = input("Ingrese el código de la golosina o 'salir' para terminar: ")
        if codigo.lower() == "salir":
            break

        codigo = int(codigo)
        encontrada = False
        for g in golosinas:
            if g[0] == codigo:
                encontrada = True
                if g[2] > 0:
                    g[2] -= 1
                    print(f"Se entregó {g[1]} a {empleados[legajo]}")

                    existe = False
                    for h in golosinasPedidas:
                        if h[0] == codigo:
                            h[2] += 1
                            existe = True
                            break
                    if not existe:
                        golosinasPedidas.append([codigo, g[1], 1])
                else:
                    print(f"Lo sentimos, {g[1]} no se encuentra disponible.")
                break
        if not encontrada:
            print("Código inválido.")


def mostrar_golosinas():
    print("\n--- Stock de golosinas ---")
    for g in golosinas:
        print(f"{g[0]} - {g[1]} (Stock: {g[2]})")
    print("--------------------------\n")


def rellenar_golosinas():
    print("Ingrese las 3 claves del técnico:")
    clave1 = input("Clave 1: ")
    clave2 = input("Clave 2: ")
    clave3 = input("Clave 3: ")

    if (clave1, clave2, clave3) != clavesTecnico:
        print("No tiene permiso para ejecutar la función de recarga")
        return

    codigo = int(input("Ingrese el código de la golosina a recargar: "))
    for g in golosinas:
        if g[0] == codigo:
            cantidad = int(input("Ingrese la cantidad a recargar: "))
            if cantidad > 0:
                g[2] += cantidad
                print(f"Se recargó {cantidad} de {g[1]}. Stock actual: {g[2]}")
            else:
                print("La cantidad debe ser mayor a cero")
            return
    print("Código inválido.")


def apagar_maquina():
    print("\n--- Historial de golosinas pedidas ---")
    total = 0
    for h in golosinasPedidas:
        print(f"{h[1]}: {h[2]} pedidas")
        total += h[2]
    print(f"Total de golosinas pedidas: {total}")
    print("Apagando máquina...")

while True:
    print("\n--- MENÚ ---")
    print("a) Pedir golosina")
    print("b) Mostrar golosinas")
    print("c) Rellenar golosinas (técnico)")
    print("d) Apagar máquina")
    opcion = input("Seleccione una opción: ")

    if opcion == "a":
        pedir_golosina()
    elif opcion == "b":
        mostrar_golosinas()
    elif opcion == "c":
        rellenar_golosinas()
    elif opcion == "d":
        apagar_maquina()
        break
    else:
        print("Opción inválida.")
