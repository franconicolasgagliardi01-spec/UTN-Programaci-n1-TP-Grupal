from leerAlumnos import leerAlumnos
from agregarAlumnos import agregarAlumno
from guardarAprobados import guardarAprobados
from pathlib import Path #Importo esta libreria para acceder al archivo

alumnos = {}

ruta = Path(__file__).parent / "alumnos.txt" #Voy a la carpeta padre del archivo.py y accedo a alumnos que se encuentra ahi

def actualizarDiccionario(alumnos): #Funcion que sirve para actualizar el diccionario en base al archivo alumnos
    with open(ruta,"r", encoding="utf-8") as archivo: #Abro el archivo, la parte de encoding es para que entienda acentos
        for linea in archivo: #Vario en funcion de las filas del archivo
            alumno = linea.strip().split(";") #Guardo la fila
            alumnos[alumno[2]] = alumno #Pongo el legajo como clave y la lista alumnos como valor

actualizarDiccionario(alumnos)

salir = False

while salir == False:
    print("-------------------------------------------------------")
    print("Seleccione una opción: \n a) Ver alumnos \n b) Agregar alumno \n c) Ver aprobados \n d) Salir\n")
    opcion = input().lower()
    print("-------------------------------------------------------")
    while opcion not in ['a', 'b', 'c', 'd']:
        print("INGRESE UNA OPCIÓN VÁLIDA")
        print("Seleccione una opción: \n a) Ver alumnos \n b) Agregar alumno \n c) Ver aprobados \n d) Salir\n")
        opcion = input().lower()

    if opcion == 'a':
        leerAlumnos() 
    elif opcion == 'b':
        agregarAlumno(alumnos)
        actualizarDiccionario(alumnos)
        pass
    elif opcion == 'c':
        guardarAprobados(alumnos)
        pass
    elif opcion == 'd':
        salir = True