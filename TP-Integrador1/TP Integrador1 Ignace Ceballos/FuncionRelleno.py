def relleno_golosinas(golosinas, codigo, cantidad_rellenar):
    # Verificar si el código está dentro de los valores permitidos
    if codigo not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        print("Código de golosina no válido")
        return  # Sale de la función si el código no es válido

    
    for i in golosinas:
        if i[0] == codigo: 
            i[2] += cantidad_rellenar  
            print(f"Stock actualizado para {i[1]}: {i[2]} unidades.")
            return  