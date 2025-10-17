from Habitacion import Habitacion

class Vivienda:

    def __init__(self, calle:str, numero:int, manzana:str, nroCasa:int, superficieTerreno:float, habitaciones:list):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = habitaciones

    def get_Metros_Cuadrados_Cubiertos(self):
        totalMetrosCubiertos = 0
        for habitacion in self.habitaciones:
            totalMetrosCubiertos += habitacion.metrosCuadrados
        if totalMetrosCubiertos < self.superficieTerreno:
            return totalMetrosCubiertos
        else:
            return print("Error: La superficie cubierta no puede ser mayor a la superficie del terreno")