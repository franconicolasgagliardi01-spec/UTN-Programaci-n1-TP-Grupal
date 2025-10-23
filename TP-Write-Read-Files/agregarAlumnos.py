from pathlib import Path

def validar_existe_alumno(legajo, alumnos): #Funcion que retorna falso si no existe el alumno en el diccionario y verdadero si existe
    if legajo in alumnos:
        return True
    else:
        return False

def agregarAlumno(alumnos):
    ruta = Path(__file__).parent / "alumnos.txt"

    # Validación de legajo
    legajo = input("Ingrese legajo (5 dígitos): ")
    while not (legajo.isdigit() and len(legajo) == 5):
        print("❌ Legajo inválido. Debe tener 5 dígitos numéricos.")
        legajo = input("Ingrese legajo válido: ")

    # Verificación de existencia
    if validar_existe_alumno(legajo, alumnos):
        print("❌ El legajo ya existe en el sistema.")
        return

    # Validación de nombre
    nombre = input("Ingrese nombre: ")
    while not nombre.isalpha():
        print("❌ Solo se permiten letras.")
        nombre = input("Ingrese nombre válido: ")

    # Validación de apellido
    apellido = input("Ingrese apellido: ")
    while not apellido.isalpha():
        print("❌ Solo se permiten letras.")
        apellido = input("Ingrese apellido válido: ")

    # Validación de nota
    nota = input("Ingrese nota (1 a 10): ")
    while not (nota.isdigit() and 1 <= int(nota) <= 10):
        print("❌ Nota inválida.")
        nota = input("Ingrese nota válida (1 a 10): ")

    # Escritura en archivo
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")
        print("✅ Alumno agregado exitosamente.")