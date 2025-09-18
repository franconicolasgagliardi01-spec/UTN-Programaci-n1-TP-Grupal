def Rellenar_Golosinas(clavesTecnico, golosinas):
    print("------------------------------")
    clave1 = input("Ingrese la primer clave: ")
    clave2 = input("Ingrese la segunda clave: ")
    clave3 = input("Ingrese la tercera clave: ")
    print("------------------------------")
    
    if clave1 == clavesTecnico[0] and clave2 == clavesTecnico[1] and clave3 == clavesTecnico[2]: #Verifico si la clave esta bien
        print("Acceso concedido")
        salir = "s"

        while salir == "s":
            codigoGolosina = int(input("Ingrese el codigo de la golosina: "))
            condicion = False

            for i in range(0,len(golosinas)): #Veo si el codigo de golosina existe
                if codigoGolosina == golosinas[i][0]:
                    condicion = True
        
            while condicion == False: #En caso de que no exista el codigo de la golosina se entra a este bucle
                print("CODIGO INVALIDO")
                codigoGolosina = int(input("Ingrese el codigo de la golosina: "))
                for i in range(0,len(golosinas)):
                    if codigoGolosina == golosinas[i][0]:
                        condicion = True
        
            cantidadGolosina = int(input("ingrese la cantidad que desea agregar: "))
            while cantidadGolosina <= 0:  #Valido la cantidad ingresada
                print("INGRESE UNA CANTIDAD VALIDA")
                cantidadGolosina = int(input("ingrese la cantidad que desea agregar: "))
        
            for i in range(0,len(golosinas)): #Cambio el valor del stock de la golosina
                if codigoGolosina == golosinas[i][0]:
                    golosinas[i][2] = golosinas[i][2] + cantidadGolosina
            
            salir = input("Desea seguir agregando stock? s/n ") #Pregunto si quiere agregar mas cosas
            while salir != "s" and salir != "n":
                print("SELECCIONE UNA OPCION VALIDA")
                salir = input("Desea seguir agregando stock? s/n ")
    else:
        print("No tiene permiso para ejecutar la función de recarga")