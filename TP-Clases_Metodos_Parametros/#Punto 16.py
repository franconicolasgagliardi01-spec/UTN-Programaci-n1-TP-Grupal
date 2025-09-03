#16
cadena = input("Ingrese una cadena: ")
tiene_numero = any(c.isdigit() for c in cadena)
print(tiene_numero)