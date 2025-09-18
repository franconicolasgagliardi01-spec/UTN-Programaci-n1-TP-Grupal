def Pedir_Golosina(empleados, golosinasPedidas, golosinas):
    print("------------------------------")
    legajo = int(input("Ingrese su legajo: "))
    print("------------------------------")

    if legajo in empleados: #Verifico que sea un empleado
        print(f"Bienvenido {empleados[legajo]}!") #Saludo al empleado
        codigoGolosina = 0

        while codigoGolosina != "salir": #Creo un bucle para decidir cuando salir

            codigoGolosina = int(codigoGolosina) #La asigno como entero ya que a partir de la segunda iteracion seria un string sino

            if codigoGolosina == 0: #Utilizo el if para que solo entre en la primer iteracion, ya que a partir de la segunda ya tengo el valor
                codigoGolosina = int(input("Ingrese el codigo de la golosina que desea: "))

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

            for i in range(0,len(golosinas)): #uso este for para encontrar la golosina
                    if codigoGolosina == golosinas[i][0]:
                        if golosinas[i][2] <= 0: #Si no hay stock se ejecuta esto
                            print(f"Lo sentimos la golosina {golosinas[i][1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
                            codigoGolosina = input()
                        else: # Modifico el stock
                            print(f"Aqui tiene: {golosinas[i][1]}")
                            golosinas[i][2] = golosinas[i][2] - 1
                            golosinasPedidas[i][2] = golosinasPedidas[i][2] + 1 #incremento en uno la cantidad de golosina pedida
                            codigoGolosina = "salir" #termino el bucle

        
    else:
        print("Usted no es un empleado de la empresa")