#Parte 2 - Punto 11
matriz = [[2.7, "hola",True] #matriz de ejemplo. El programa funciona con multiples tamaños
        , [False,55,"chau"]
        , ["Mundo",3.14,True]]

def posicion_valida(matriz, fila, columna): #Funcion que me dice si una pocicion en una matriz existe
    return (
        0 <= fila < len(matriz) and
        0 <= columna < len(matriz[fila])
    )

matriz_90 = []
aux = [] #Arreglo auxiliar que me servira para guardar las filas de la nueva matriz 90 grados rotada
tamaño = len(matriz) #Busco cantidad de filas de la matriz
tamaño_fila = 0

for fila in matriz:  #busco la fila con mas elementos de la matriz
    if len(fila) > tamaño_fila:
        tamaño_fila = len(fila)

for i in range(0,tamaño_fila):
    for j in range(0,tamaño):
        if posicion_valida(matriz,j,i): #Veo si la pocicion existe en la matriz
            aux.append(matriz[j][i]) #Guardo las columnas
        else:
            aux.append("")
    aux.reverse() #Las doy vuelta para cumplir con el sentido horario
    matriz_90.append(aux.copy()) # le asigno la primer fila a la matriz rotada 90 grados, copy() sirve para luego poder reutilizar aux
    aux.clear() #Elimino el contenido de aux para reutilizarla en la siguiente iteracion 

tamaño_nuevo = len(matriz_90)
for i in range(0,tamaño_nuevo): #imprimo fila por fila la nueva matriz
    print(matriz_90[i])