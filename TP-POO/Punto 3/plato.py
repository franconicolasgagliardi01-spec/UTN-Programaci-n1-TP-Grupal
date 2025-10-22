from ingrediente import Ingrediente


class Plato:
    def __init__(self, nombre_completo: str, precio: float, es_bebida: bool):
        self.nombre_completo = nombre_completo.strip().title()
        self.precio = precio
        self.es_bebida = es_bebida
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)

    def tiene_ingredientes(self):
        return len(self.ingredientes) > 0

    def mostrar_info(self):
        print(self.nombre_completo)
        print(f"Precio: $ {self.precio}")
        if not self.es_bebida:
            print("Ingredientes:")
            print("Nombre\t\tCantidad\tUnidad de Medida")
            for ing in self.ingredientes:
                print(f"{ing.nombre}\t{ing.cantidad}\t{ing.unidad_medida}")
        print("----------------------------------")
