"""7- Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas
vocales tiene en total."""

cadena = input("Ingrese una cadena de texto: ")

longitud = len(cadena)
print("El tamaño de la cadena es:", longitud)


vocales = "aeiouAEIOU"
contador_vocales = 0

for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

print("La cantidad de vocales en la cadena es:", contador_vocales)
