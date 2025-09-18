def Mostrar_Golosinas(golosinas, golosinasPedidas, opcion):
    print("------------------------------")
    print("[Codigo, Nombre, Cantidad]")
    for i in range(0,len(golosinas)): #Muestro todas las golosinas fila por fila
        print(golosinas[i])

    if opcion == "d": #En caso de que se apague
        largoGolosinasPedidas = len(golosinasPedidas) #Guardo la cantidad de filas de golosinasPedidas
        totalPedido = 0 #Donde hare la sumatoria

        for i in range(0,largoGolosinasPedidas): #Recorro la lista golosinasPedidas guardando la cantidad
            totalPedido = totalPedido + golosinasPedidas[i][2] 
        
        print(f"El total de golosinas pedidas fue de: {totalPedido}")
        print("¡Adios!")