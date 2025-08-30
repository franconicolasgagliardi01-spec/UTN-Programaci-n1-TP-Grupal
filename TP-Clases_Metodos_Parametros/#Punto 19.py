#Punto 19
class OperacionMatematica:
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def sumarNumeros(self):
        print("Suma: ",self.valor1 + self.valor2)
    
    def restarNumeros(self):
        print("Resta: ",self.valor1 - self.valor2)
    
    def multiplicarNumeros(self):
        print("Multiplicacion: ",self.valor1 * self.valor2)
    
    def dividirNumeros(self):
        print("Division: ",self.valor1 / self.valor2)
    
    def aplicarOperacion(self,operacion):
        if operacion == "+":
            self.sumarNumeros()
        elif operacion == "-":
            self.restarNumeros()
        elif operacion == "*":
            self.multiplicarNumeros()
        elif operacion == "/":
            self.dividirNumeros()
        else:
            print("Ingrese una operacion valida...")

class Calculo:
    def main():
        val1 = int(input("Ingrse el primer numero: "))
        val2 = int(input("Ingrse el segundo numero: "))
        OPMatematica1 = OperacionMatematica(val1,val2)
        OPMatematica1.aplicarOperacion("+")
        OPMatematica1.aplicarOperacion("-")
        OPMatematica1.aplicarOperacion("*")
        OPMatematica1.aplicarOperacion("/")

calcular = Calculo
calcular.main()