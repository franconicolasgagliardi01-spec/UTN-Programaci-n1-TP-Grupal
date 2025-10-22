class Ingrediente:
    def __init__(self, nombre: str, cantidad: float, unidad_medida: str):
        self.nombre = nombre.strip().title()
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida.strip()

    def __str__(self):
        return f"{self.nombre} {self.cantidad} {self.unidad_medida}"
