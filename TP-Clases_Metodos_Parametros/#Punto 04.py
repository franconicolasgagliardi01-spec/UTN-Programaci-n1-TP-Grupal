#4 Desarrolle un programa que ayude a una cajera a determinar el número de billetes y 
#monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50, 
#20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de 
#dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete 
#de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05 
#centavos. Plantee el algoritmo planteando métodos para su resolución. 

def calcular_billetes_y_monedas(cantidad):
    billetes = [200, 100, 50, 20, 10, 5, 2, 1]
    monedas = [0.50, 0.25, 0.10, 0.05]

    print("\n=== DESGLOSE DEL DINERO ===")
    print(f"Cantidad ingresada: ${cantidad:.2f}\n")

    for billete in billetes:
        cantidad_billetes = int(cantidad // billete)
        if cantidad_billetes > 0:
            print(f"{cantidad_billetes} billete(s) de ${billete}")
            cantidad = cantidad % billete

    for moneda in monedas:
        cantidad_monedas = int(round(cantidad / moneda, 2) // 1)
        if cantidad_monedas > 0:
            print(f"{cantidad_monedas} moneda(s) de ${moneda:.2f}")
            cantidad = round(cantidad % moneda, 2)

    if cantidad > 0:
        print(f"Faltante: ${cantidad:.2f}")


dinero = float(input("Ingrese la cantidad de dinero: "))
calcular_billetes_y_monedas(dinero)