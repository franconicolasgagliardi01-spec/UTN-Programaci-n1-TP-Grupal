def mostrarNotas(alumnos, materias):
    print("\nNotas ingresadas por materia:")

    for legajo, nombre in alumnos.items():
        print(f"\nAlumno: {nombre} (Legajo: {legajo})")
        mejor_materia = ""
        mejor_nota = -1

        for materia in materias:
            notas = materia["notas"].get(legajo, [])
            print(f"  {materia['asignacion']}: {notas}")

            if notas:
                nota_max = max(notas)
                if nota_max > mejor_nota:
                    mejor_nota = nota_max
                    mejor_materia = materia["asignacion"]

        if mejor_materia:
            print(f"Materia con mayor nota: {mejor_materia} ({mejor_nota})")
        else:
            print("No hay notas registradas para este alumno.")