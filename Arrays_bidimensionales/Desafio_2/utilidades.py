
def inicializar_matriz(cantidad_filas: int,
                       cantidad_columnas: int,
                       valor_por_defecto = False)->list:
    
    '''
    '''

    matriz = []

    for _ in range(cantidad_filas):
        fila = [valor_por_defecto] * cantidad_columnas

        matriz += [fila]

    return matriz


def mostrar_matriz(matriz: list,
                   mensaje_final = "")-> None:
    '''
    Muestra el contenido de la matriz.
    '''

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]}" + mensaje_final, end=" ")
        print("")


