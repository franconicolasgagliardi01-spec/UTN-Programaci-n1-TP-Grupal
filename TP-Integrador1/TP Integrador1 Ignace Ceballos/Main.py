#Comenzamos el programa haciendo la lista de elementos que va a contener nuestra maquina de golosinas
import FuncionPedidos
import FuncionMostrar
import FuncionRelleno
import FuncionSuma

golosinas = [
    [1, "Kitkat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 50],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

empleados = [
    [1100, "Alonso Mazza"],
    [1200, "Taylor Swift"],
    [1300, "Ed Warren"],
    [1400, "Xavi Hernandez"],
    [1500, "Cazzu"]
]

golosinasPedidas = [[]]

listacontraseña = [3]

clavestecnico = ("Admin", 1899, 2025)

print("-----------------------------------------------------------------")
print("BIENVENIDO A LA MAQUINA DE GOLOSINAS, ¿COMO TE PUEDO AYUDAR HOy?")
print("-----------------------------------------------------------------")

letra = ""

condicion = False

acceso = 0

cantidad_rellenar = 0


while condicion != True:


    print("Las opciones del sistema son:")
    print("Escriba a para poder pedir una golosina")
    print("Escriba b para poder ver todas las golosinas con sus cantidades actuales")
    print("Escriba c para rellenar el stock de golosinas")
    print("Ingrese d para apagar el sistema")
    letra = input("")


    if letra == "a" or letra == "A":
        legajo = int(input("Porfavor ingrese su legajo de empleado: "))
          #Confirmamos que el empleado tenga permiso para retirar golosinas
        for i in empleados:
            if i[0] == legajo:
                print(golosinas)
                
                codigo = int(input("Elija la golosina que desea retirar mediante su numero de id (1,12) "))
                
                cantidad = int(input("Ingrese la cantidad que quiere retirar mirando el numero a la derecha del producto "))
                
                FuncionPedidos.registrar_Pedido(codigo,cantidad,golosinas,golosinasPedidas)
                
                permiso = True
                break
            permiso = False
        if permiso == False:
            print("Legajo incorrecto, porfavor intentelo mas tarde")

    if letra == "b" or letra == "B":
         FuncionMostrar.mostrar_golosinas(golosinas)

    if letra == "c" or letra == "C":
        listacontraseña = input("Ingrese las 3 contraseñas (separadas por coma): ").split(',')

        for i in listacontraseña:
            for i in listacontraseña:
              if i in clavestecnico:  # Asegúrate de eliminar espacios extra
               acceso += 1

              if acceso == 3:
                break
              
        if acceso == 3:
            print(golosinas)
            codigo = int(input("Elija la golosina que desea relleno mediante su numero de id (1,12) "))
            cantidad_rellenar = int(input("Ingrese la cantidad que quiere rellenar "))
            FuncionRelleno.relleno_golosinas(golosinas,codigo,cantidad_rellenar)
        else: 
            print("“No tiene permiso para ejecutar la función de recarga”")

    if letra == "d" or letra == "D":
        print(golosinasPedidas)

        FuncionSuma.suma_columna(golosinasPedidas)

        condicion = True




    




            


