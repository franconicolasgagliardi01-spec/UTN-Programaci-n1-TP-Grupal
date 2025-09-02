#13- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se 
#encuentra dentro de la primera. 

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

if cadena2 in cadena1:
    print("La segunda cadena se encuentra dentro de la primera.")
else:
    print("La segunda cadena NO se encuentra dentro de la primera.")