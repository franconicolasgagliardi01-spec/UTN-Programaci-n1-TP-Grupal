"""Lógica a Implementar:
El algoritmo debe permitir cargar la marca y el modelo de una computadora y para cada
computadora indicar los N componentes de CPU que posee indicando la cantidad y el
precio por ejemplo componente “Memoria RAM 2 Gb”, marca “Kingston”, cantidad “2”,
precio “8000”
Al finalizar la carga de los componentes mostrar la información cargada, y determinar el
costo de la computadora el cual será el equivalente de sumar el precio por la cantidad
usada de cada componente y el precio de venta sugerido para la computadora el cual será
equivalente a el precio de costo más el 40% del precio de costo si el precio de costo es
menor a 50000, o equivalente a el precio de costo más el 30% del precio de costo si el
precio de costo es mayor a 50000.
Al terminar de mostrar los datos y precio de la computadora deberá preguntar si desea
cotizar una nueva computadora, si la respuesta es “SI” deberá iniciar nuevamente el
programa, si la respuesta es “NO”, terminar la ejecución del programa.
"""

from ComponenteCPU import ComponenteCPU
from Computadora import Computadora


class CostoComputadora:
    def main():

        objetos= []
        opcion = "SI"
        while opcion == "SI":
          
          print("==================================================")
          print("---CARGA COMPUTADORA---")

          marcaPC = input("Ingrese la marca de la computadora -> ")

          modeloPC = input("Ingrese el modelo de la computadora -> ")

          cantidadcomponentes = int(input("Porfavor ingrese cuantos componentes desea agregar a la PC: "))

          for i in range (0,cantidadcomponentes):
              print(f"\n-- Componente {i} --")
              componente = input(f"Ingresa el componente -> ")
              marca = input("Ingrese la marca -> ")
            
              cantidad = int(input("Ingrese su cantidad -> "))
              while cantidad < 1:
                  cantidad = int(input("Ingrese una cantidad mayor a 0 -> "))
              
              
              precio = float(input("Ingrese su precio -> "))
              while precio < 1:
                  precio = float(input("Ingrese un precio mayor a 0 -> "))
             
              a = ComponenteCPU(componente, marca, cantidad, precio)

              objetos.append(a)
          
          compu = Computadora(marcaPC, modeloPC, objetos)
          costo_total = 0

          for obj in objetos:
              costo_total += obj.precio * obj.cantidad

          if costo_total < 50000:
              precio_venta = costo_total * 1.4
          else:
             precio_venta = costo_total * 1.3

    
          print("====================================")
          print(f"Computadora: {compu.marca} - Modelo: {compu.modelo}")
          print("Componentes:")
          for o in objetos:
                print(f"  - {o.componente} ({o.marca}) cantidad: {o.cantidad} -> ${o.precio}")
                
                
          print(f"\nCosto total: ${costo_total}")
          print(f"Precio de venta sugerido: ${precio_venta}")
          print("====================================")
          
          opcion = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ")
          opcion = opcion.upper()
                
        print("\nPrograma finalizado. ¡Gracias!")


CostoComputadora.main()

                  

             







          




    