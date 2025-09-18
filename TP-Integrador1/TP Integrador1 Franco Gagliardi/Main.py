from Mostrar import Mostrar_Golosinas #importo las funciones de otros archivos
from Rellenar import Rellenar_Golosinas
from Pedir import Pedir_Golosina

golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

clavesTecnico = ("admin","CCCDDD","2020")

golosinasPedidas = [
    [1, "KitKat", 0],
    [2, "Chicles", 0],
    [3, "Caramelos de Menta", 0],
    [4, "Huevo Kinder", 0],
    [5, "Chetoos", 0],
    [6, "Twix", 0],
    [7, "M&M'S", 0],
    [8, "Papas Lays", 0],
    [9, "Milkybar", 0],
    [10, "Alfajor Tofi", 0],
    [11, "Lata Coca", 0],
    [12, "Chitos", 0]
]

salir = False #Variable que usare para apagar la maquina

print("¡Bienvenido!")

while salir == False:
    print("------------------------------")
    print("a. Pedir golosina")
    print("b. Mostrar golosinas")
    print("c. Rellenar golosinas")
    print("d. Apagar maquina")
    print("------------------------------")
    opcion = input()

    while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d": #Validacion de opcion
        print("------------------------------")
        print("INGRESE UN VALOR VALIDO")
        print("a. Pedir golosina")
        print("b. Mostrar golosinas")
        print("c. Rellenar golosinas")
        print("d. Apagar maquina")
        print("------------------------------")
        opcion = input()
    
    if opcion == "a": #Llamo a la funcion que pide golosinas
        Pedir_Golosina(empleados, golosinasPedidas, golosinas)
    elif opcion == "b": #Llamo a la funcion que muestra las golosinas pedidas
        Mostrar_Golosinas(golosinas, golosinasPedidas, opcion)
    elif opcion == "c": #Llamo a la funcion para rellenar las golosinas
        Rellenar_Golosinas(clavesTecnico, golosinas)
    else: #Apago la maquina, llamo a la funcion que muestra las golosinas pedidas y muesto la cantidad total
        Mostrar_Golosinas(golosinas, golosinasPedidas, opcion)
        salir = True
