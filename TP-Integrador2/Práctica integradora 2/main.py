from gestionarNotas import gestionarNotas
from mostrarNotas import mostrarNotas
from notasFinales import notasFinales

alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

materias = [
    {"asignacion": "Ciencias", "notas": {}},
    {"asignacion": "Historia", "notas": {}},
    {"asignacion": "Matemática", "notas": {}},
    {"asignacion": "Física", "notas": {}}
]

print("Bienvenido al sistema integral de gestión de notas\n")

salir = False
while not salir:
    opcion = input("Seleccione la opción deseada:\n"
                   "(a) Gestionar notas\n"
                   "(b) Mostrar notas\n"
                   "(c) Mostrar notas finales\n"
                   "(d) Salir del sistema\n\n")

    while opcion.lower() not in ["a", "b", "c", "d"]:
        print("SELECCIONE UNA OPCIÓN VÁLIDA: (a) - (b) - (c) - (d)")
        opcion = input("Seleccione la opción deseada:\n"
                       "(a) Gestionar notas\n"
                       "(b) Mostrar notas\n"
                       "(c) Mostrar notas finales\n"
                       "(d) Salir del sistema\n")

    if opcion.lower() == "a":
        gestionarNotas(materias, alumnos)

    elif opcion.lower() == "b":
        mostrarNotas(alumnos, materias)

    elif opcion.lower() == "c":
        notasFinales(alumnos, materias)

    elif opcion.lower() == "d":
        salir = True
        print("Cerrando sistema de gestión de notas")