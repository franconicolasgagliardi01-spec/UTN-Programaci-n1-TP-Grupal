from pathlib import Path
def guardarAprobados(alumnos):
    ruta = Path(__file__).parent / "aprobados.txt"
    legajos = list(alumnos) #Creo lista con legajos
    aprobados = {}

    for i in range(len(legajos)): #Vario en funcion de los legajos para encontrar aprovados
        if int(alumnos[legajos[i]][3]) >= 6: #Veo si la nota es aprobada
            aprobados[legajos[i]] = [alumnos[legajos[i]][0] + " " + alumnos[legajos[i]][1], alumnos[legajos[i]][3]] #Pongo legajo como clave y nombre como valor

    legajosAprobados = list(aprobados)

    with open(ruta, "w", encoding="utf-8") as archivo: #Creo archivo de aprobados
        for i in range(len(legajosAprobados)):
            aux = aprobados[legajosAprobados[i]]
            archivo.write(f"{legajosAprobados[i]};{aux[0]};{aux[1]}\n")

    with open(ruta, "r", encoding="utf-8") as archivoAprobados: #Leo archivo de aprobados
        print("Alumnos aprobados: ")
        for linea in archivoAprobados:
            linea = linea.strip()
            if linea != "":
                legajo, nombre, nota = linea.split(";")
                print(f"{nombre} con legajo: {legajo} y nota: {nota} \n")


