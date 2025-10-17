from pathlib import Path
def leerAlumnos():
    print("\nAlumnos:\n")

    ruta = Path(__file__).parent / "alumnos.txt"
    # Lee el archivo y muestra los alumnos
    with open(ruta, "r", encoding="utf-8") as archivoAlumnos:
        for linea in archivoAlumnos:
            linea = linea.strip()
            if linea != "":
                nombre, apellido, legajo, nota = linea.split(";")
                print(f"{nombre} {apellido} - Legajo: {legajo} - Nota: {nota}\n")

