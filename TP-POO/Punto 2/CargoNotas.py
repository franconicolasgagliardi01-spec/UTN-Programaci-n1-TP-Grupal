"""Lógica a Implementar:
En la clase CargaNotas debera declarar una variable que permita contener un conjunto de
Alumnos:
Ejemplo:
alumnos = []
El algoritmo debe permitir cargar N cantidad de alumnos y para cada alumno N cantidad
de Notas. Al finalizar la carga de los alumnos y sus notas mostrar la información cargada y
para cada alumno mostrar el promedio de las notas que posee. Valide que se ingrese al
menos 1 nota. Agregue en la clase Alumno un método que calcule el promedio de las
notas que posee."""

from Nota import Nota
from Alumno import Alumno

class CargaNotas:
    def main():
        alumnos = []
        legajos_usados = set()
        print("==================================================")
        print("---Carga de alumnos---")

        cantidadAlumnos = int(input("-Ingrese la cantidad de alumnos a los que le quiere ingresar notas: ")) 

        for i in range(1, cantidadAlumnos + 1):
           
            print(f"\n-- Alumno {i} --")
            nombreCompleto = input(f"-Ingrese el nombre completo del alumno {i}: ")
            aux = nombreCompleto.replace(" ","")
            while not aux.isalpha():
                nombreCompleto = input(f"-Ingrese un nombre completo valido para el alumno {i}: ")
                aux = nombreCompleto.replace(" ","")
                
            legajo = input("-Ingrese el legajo de este alumno: ")

            while legajo in legajos_usados:
                print(" Ya existe un alumno con este legajo. Intente con otro.")
                legajo = input("-Ingrese un legajo diferente: ")

            legajos_usados.add(legajo)


            legajocorrecto = False

            if legajo.isdigit() and len(legajo) == 5:
                legajocorrecto = True

            while legajocorrecto == False:
            
                print(" Error: El legajo debe  solo números y tener 5 dígitos.")
                legajo = input()
            
                if legajo.isdigit() and len(legajo) == 5:
                    legajocorrecto = True
                else: 
                    print(" Error: El legajo debe  solo números y tener 5 dígitos.")


            a = Alumno(nombreCompleto, legajo)

            cantidadNotas = int(input("-Ingrese la cantidad de notas para este alumno (mínimo 1): "))
            while cantidadNotas < 1:
                cantidadNotas = int(input("Debe ingresar al menos 1 nota. Intente nuevamente: "))

            for j in range(1, cantidadNotas + 1):
                print(f"  --Sección Nota {j}--")
                catedra = input("-Ingrese la cátedra: ")
                notaExamen = float(input("-Ingrese la nota: "))

                while notaExamen < 1 or notaExamen > 10:
                    notaExamen = float(input("Ingrese una nota valida (entre 1 y 10): "))

                n = Nota(catedra, notaExamen)
                a.agregar_nota(n)

            alumnos.append(a)
            
        print("\n================================================================")
        print("---RESULTADOS FINALES---")
        for a in alumnos:
            print(f"\nAlumno: {a.nombre_completo} (Legajo: {a.legajo})")
            for n in a.notas:
                print(f"  Cátedra: {n.catedra} - Nota: {n.notaExamen}")
            print(f"  Promedio: {a.calcular_promedio()}")


CargaNotas.main()
