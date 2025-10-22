from plato import Plato
from ingrediente import Ingrediente


def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print(" El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print(" Por favor, ingrese un número válido.")


def pedir_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print(" Este campo no puede estar vacío.")


def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje + " (s/n): ").lower().strip()
        if respuesta in ("s", "n"):
            return respuesta == "s"
        print(" Responda con 's' o 'n'.")


def main():
    platos_menu = []

    while True:
        print("\n--- CARGA DE NUEVO PLATO ---")
        nombre = pedir_no_vacio("Ingrese el nombre del plato: ")
        precio = pedir_float("Ingrese el precio del plato: ")
        es_bebida = pedir_si_no("¿Es una bebida?")

        plato = Plato(nombre, precio, es_bebida)

        if not es_bebida:
            print("\n--- Carga de ingredientes ---")
            while True:
                nombre_ing = pedir_no_vacio("Nombre del ingrediente: ")
                cantidad = pedir_float("Cantidad: ")
                unidad = pedir_no_vacio("Unidad de medida: ")

                ingrediente = Ingrediente(nombre_ing, cantidad, unidad)
                plato.agregar_ingrediente(ingrediente)

                if not pedir_si_no("¿Desea agregar otro ingrediente?"):
                    if not plato.tiene_ingredientes():
                        print(" Debe ingresar al menos un ingrediente.")
                        continue
                    break
        else:
            print("Plato registrado como bebida (sin ingredientes).")

        platos_menu.append(plato)

        if not pedir_si_no("¿Desea agregar otro plato?"):
            break

    print("\n----------- MENÚ ----------------")
    for p in platos_menu:
        p.mostrar_info()


if __name__ == "__main__":
    main()
