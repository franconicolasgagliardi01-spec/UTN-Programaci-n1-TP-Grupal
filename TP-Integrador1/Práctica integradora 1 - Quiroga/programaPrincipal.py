#Programa principal

#importo las funciones desde el archivo principal
from funcionPedir import pedirGolosinas 
from funcionMostrar import mostrarLista
from funcionRellenar import rellenarGolosinas
from funcionApagar import apagarMaquina

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Lista de golosinas
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de menta", 50],
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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Lista de empleados
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Contraseña de técnico
clavesTecnico = ("admin", "CCCDDD", "2020")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Lista para registrar las golosinas pedidas
golosinasPedidas = ["fila", "Denominación golosina", "Cantidad total pedida"]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Bucle de control de opciones
salida = False
while salida == False:
    opcion = input("Seleccione la opción deseada: (a) Pedir golosina -  (b) Mostrar lista - (c) Rellenar golosinas - (d) Apagar máquina \n")
    if opcion == "a" or opcion == "A":
        pedirGolosinas(golosinas, empleados, golosinasPedidas)

    if opcion == "b" or opcion == "B":
        mostrarLista(golosinas)

    if opcion == "c" or opcion == "C":
        rellenarGolosinas(clavesTecnico, golosinas)
        
    if opcion == "d" or opcion == "D":
       apagarMaquina(golosinasPedidas)