"""3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
14. Plantee el algoritmo planteando métodos para su resolución."""

def ingresar_numero():
    numero = int(input("Ingrese un número de 3 dígitos (100-999): "))
    return numero

def calcular_suma_digitos(numero):

    #El nombre de cada variable es porque va de derecha a izquierda el orden del numero
    
    primernum = numero % 10      # Último dígito
    numero = numero // 10 # Quitar último dígito


    segundonum = numero % 10      # Segundo dígito
    numero = numero // 10 # Quitar segundo dígito

    tercernum = numero % 10      # Primer dígito

    return primernum + segundonum + tercernum

def principal():
    numero = ingresar_numero()
    suma = calcular_suma_digitos(numero)
    print(f"La suma de los dígitos es: {suma}")

# Ejecutar el programa
principal()