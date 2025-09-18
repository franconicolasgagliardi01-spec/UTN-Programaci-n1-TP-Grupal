def registrar_Pedido(codigo, cantidad,golosinas,golosinasPedidas):
    
    # Buscar golosina en lista de golosinas
    for i in golosinas:
        if i[0] == codigo:
            nombre = i[1]
            stock =  i[2]

            # Verificar stock
            if stock >= cantidad:
                # Descontar stock
                i[2] -= cantidad
                print(f"✅ Pedido registrado: {cantidad} x {nombre}")

                golosinasPedidas.append([codigo, nombre, cantidad])
            else:
                print(f"❌ No hay stock suficiente de {nombre}. Disponible: {stock}")
            return
    print("❌ Código de golosina no encontrado")

    return print("Golosina no encontrada")