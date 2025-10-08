def notasFinales(alumnos, materias):
    print("\nPromedios generales por alumno:")
    mejor_legajo = None
    mejor_promedio = -1

    for legajo, nombre in alumnos.items():
        total = 0
        cantidad = 0
        for materia in materias:
            notas = materia["notas"].get(legajo, [])
            total += sum(notas)
            cantidad += len(notas)
        if cantidad > 0:
            promedio = total / cantidad
            print(f"  {legajo} - {nombre}: {promedio:.2f}")
            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor_legajo = legajo
        else:
            print(f"  {legajo} - {nombre}: sin notas registradas")

    if mejor_legajo is not None:
        print(f"\nMejor promedio: {alumnos[mejor_legajo]} ({mejor_promedio:.2f})")
    else:
        print("\nNo hay notas registradas para calcular el mejor promedio\n")