from Vivienda import Vivienda

class Barrio:

    def __init__(self, nombre:str , empresaConstructora:str, viviendas:list ): #Definicion de atributos de la clase
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = viviendas
    
    def get_Superficie_TotalTerreno(self): #Funcion que devuelve la superficie total del barrio
        terrenoTotal = 0
        for vivienda in self.viviendas:
            terrenoTotal += vivienda.superficieTerreno
        return terrenoTotal

    def get_Superficie_Total_TerrenoXManzana(self,manzana): #Funcion que devuelve la superficie total de una manzana especifica
        terrenoTotal = 0
        for vivienda in self.viviendas:
            if vivienda.manzana == manzana:
                terrenoTotal += vivienda.superficieTerreno
        return terrenoTotal
    
    def get_Superficie_Total_Cubierta(self): #Funcion que devuelve la superficie total cubierta del barrio
        superficieTotal = 0
        for vivienda in self.viviendas:
            superficieTotal += vivienda.get_Metros_Cuadrados_Cubiertos()
        return superficieTotal