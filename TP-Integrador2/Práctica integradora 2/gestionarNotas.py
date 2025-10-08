def gestionarNotas(materias, alumnos):
    for legajo in alumnos:
        print(f"\nAlumno:{alumnos[legajo]} (Legajo: {legajo})")
        for materia in materias:
            print(f"\nAsignación: {materia['asignacion']}")
            notas = []
            for i in range(2):
                valor = -1
                while valor < 0 or valor > 10:
                    valor = float(input(f"Ingrese nota {i + 1}: "))
                    if valor < 0 or valor > 10:
                        print("La nota debe ser mayor a 0 y menor a 10. Intente nuevamente.")
                notas.append(valor)
            materia["notas"][legajo] = notas