def suma_columna(golosinasPedidos):
    largoGolosinasPedidos = len(golosinasPedidos)  # Guardo la cantidad de filas de golosinasPedidos
    totalPedido = 0 

    for i in range(largoGolosinasPedidos):  # Recorro la lista golosinasPedidos
        print(f"Retiro numero: {i}: {golosinasPedidos[i]}")  # Imprimir la sublista actual
        if len(golosinasPedidos[i]) > 2:  # Verifico que la sublista tenga al menos 3 elementos
            print(f"Valor a sumar: {golosinasPedidos[i][2]}")  # Imprimir el valor que voy a sumar
            totalPedido += golosinasPedidos[i][2]  # Sumando el último valor de cada lista interna

    print(f"Total Pedido: {totalPedido}")
    return totalPedido