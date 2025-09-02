#10- Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario  
#pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el 
#resultado por pantalla.  

cadena = input("Ingrese una cadena: ")
opcion = input("¿Desea convertir a mayúsculas (mayusculas) o minúsculas (minusculas)? ")

if opcion.upper() == "mayusculas":
    print("Cadena en mayúsculas:", cadena.upper())
elif opcion.lower() == "minusculas":
    print("Cadena en minúsculas:", cadena.lower())
else:
    print("Opción no válida.")