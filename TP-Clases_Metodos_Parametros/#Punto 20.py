#Punto 20
import math

def mcm(a, b):
    return abs(a * b) // math.gcd(a, b) #Funcion para obtener el minimo comun multiplo

class Fraccion:
    def __init__(self,numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def sumarFracciones(self,otra):
        nuevo_den = mcm(self.denominador,otra.denominador)
        nuevo_num = (self.numerador * nuevo_den//self.denominador) + (otra.numerador * nuevo_den//otra.denominador)
        return Fraccion(nuevo_num,nuevo_den)
    
    def restarFracciones(self,otra):
        nuevo_den = mcm(self.denominador,otra.denominador)
        nuevo_num = (self.numerador * nuevo_den//self.denominador) - (otra.numerador * nuevo_den//otra.denominador)
        return Fraccion(nuevo_num,nuevo_den)
    
    def multiplicarFracciones(self,otra):
        nuevo_den = self.denominador * otra.denominador
        nuevo_num = self.numerador * otra.numerador 
        max_divisor = 0
        #simplifico la fraccion
        max_divisor = math.gcd(nuevo_den, nuevo_num)
        nuevo_num = int(nuevo_num/max_divisor)
        nuevo_den = int(nuevo_den/max_divisor)

        return Fraccion(nuevo_num,nuevo_den)
    
    def dividirFracciones(self,otra):
        nuevo_den = self.denominador * otra.numerador
        nuevo_num = self.numerador * otra.denominador 
        max_divisor = 0

        #simplifico la fraccion
        max_divisor = math.gcd(nuevo_den, nuevo_num)
        nuevo_num = int(nuevo_num/max_divisor)
        nuevo_den = int(nuevo_den/max_divisor)

        return Fraccion(nuevo_num,nuevo_den)

class OperacionesFraccion:
    def main(self):
        num1 = int(input("Ingrse el numerador de la primer fraccion: "))
        den1 = int(input("Ingrse el denominador de la primer fraccion: "))
        while den1 == 0:
            print("EL DENOMINADOR NO PUDE SER 0")
            den1 = int(input("Ingrse el denominador de la primer fraccion: "))
        num2 = int(input("Ingrse el numerador de la segunda fraccion: "))
        den2 = int(input("Ingrse el denominador de la segunda fraccion: "))
        while den2 == 0:
            print("EL DENOMINADOR NO PUDE SER 0")
            den2 = int(input("Ingrse el denominador de la primer fraccion: "))

        f1 = Fraccion(num1,den1)
        f2 = Fraccion(num2, den2)

        sumaFraccion = f1.sumarFracciones(f2)
        restaFracciones = f1.restarFracciones(f2)
        multiplicacionFracciones = f1.multiplicarFracciones(f2)
        divisionFracciones = f1.dividirFracciones(f2)

        print(f"La suma de las fracciones es: {sumaFraccion.numerador}/{sumaFraccion.denominador}")
        print(f"La resta de las fracciones es: {restaFracciones.numerador}/{restaFracciones.denominador}")
        print(f"La multiplicacion de las fracciones es: {multiplicacionFracciones.numerador}/{multiplicacionFracciones.denominador}")
        print(f"La division de las fracciones es: {divisionFracciones.numerador}/{divisionFracciones.denominador}")

OPFraccion = OperacionesFraccion()
OPFraccion.main()