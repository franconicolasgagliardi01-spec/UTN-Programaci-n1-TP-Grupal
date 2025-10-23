from Barrio import Barrio 
from Vivienda import Vivienda 
from Habitacion import Habitacion

barrios = []
barriosIngresados = []

creacion = True
while creacion: #Estructura principal creacion de barrios
    print("*Creacion de barrio*")
    nombre = input("Ingrese el nombre del barrio: ")
    while nombre in barriosIngresados:
        print("El barrio ingresado ya existe")
        nombre = input("Ingrese el nombre del barrio: ")
    barriosIngresados.append(nombre)

    empresa = input("ingrese el nombre de la empresa constructora: ")
    viviendas = []
    barrio_1 = Barrio(nombre, empresa, viviendas)

    creacion1 = True
    while creacion1: #Estructura secundaria de creacion de viviendas
        print("*Creacion de vivienda*")
        calle = input("Ingrese la calle: ")  

        numero = input("Ingrese el número de calle: ")
        while not numero.isdigit():
            print("Ingrese un numero")
            numero = input("Ingrese el número de calle: ") 
        numero = int(numero)

        manzana = input("Ingrese la manzana: ")  
        nroCasa = input("Ingrese el número de casa: ")
        while not nroCasa.isdigit():
            print("Ingrese un numero")
            nroCasa = input("Ingrese el número de casa: ") 
        nroCasa = int(nroCasa)  

        superficieTerreno = input("Ingrese la superficie del terreno en m²: ")
        while not superficieTerreno.isdigit():
            print("Ingrese un numero")
            superficieTerreno = input("Ingrese la superficie del terreno en m²: ")
        superficieTerreno = float(superficieTerreno)

        habitaciones = []
        vivienda_1 = Vivienda(calle, numero, manzana, nroCasa, superficieTerreno, habitaciones)
        barrio_1.viviendas.append(vivienda_1)

        creacion2 = True
        while creacion2: #Estructura terciaria de creacion de habitaciones
            print("*Creo habitacion*")
            nombre = input("Ingrese el nombre de la habitacion: ")

            metrosCuadrados = input("Ingrese los metros cuadrados de la habitacion: ")
            while not metrosCuadrados.isdigit():
                print("Ingrese un numero")
                metrosCuadrados = input("Ingrese los metros cuadrados de la habitacion: ")
            metrosCuadrados = float(metrosCuadrados)
            
            habitacion_1 = Habitacion(nombre, metrosCuadrados)
            vivienda_1.habitaciones.append(habitacion_1)

            opcion = input("Desea seguir creando habitaciones para esta vivienda? s/n: ")
            while opcion.lower() != "s" and opcion.lower() != "n":
                print("Seleccione una opcion valida")
                opcion = input("Desea seguir creando habitaciones para esta vivienda? s/n: ")
            if opcion.lower() == "n":
                creacion2 = False
        
        opcion = input("Desea seguir creando viviendas para este barrio? s/n: ")
        while opcion.lower() != "s" and opcion.lower() != "n":
            print("Seleccione una opcion valida")
            opcion = input("Desea seguir creando viviendas para este barrio? s/n: ")
        if opcion.lower() == "n":
            creacion1 = False

    barrios.append(barrio_1) #Guardo el barrio 

    opcion = input("Desea seguir creando barrios? s/n: ")
    while opcion.lower() != "s" and opcion.lower() != "n":
        print("Seleccione una opcion valida")
        opcion = input("Desea seguir creando barrios? s/n: ")
    if opcion.lower() == "n":
        creacion = False

for barrio in barrios:
    print(f"El barrio {barrio.nombre}, tiene un terreno de: {barrio.get_Superficie_TotalTerreno()}")
    manzana = input("Ingrese la manzana de la que desea calcular el terreno: ")
    print(f"Y tiene en la manzana {manzana} un terreno de: {barrio.get_Superficie_Total_TerrenoXManzana(manzana)}")
    print(f"Y tiene un total de {barrio.get_Superficie_Total_Cubierta()} metros cuadrados cubiertos")

print("Adios..")
