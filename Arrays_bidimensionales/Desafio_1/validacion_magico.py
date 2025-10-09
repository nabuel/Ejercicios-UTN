import random
import funciones_matriz


matriz = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]

def calcular_constante_magica(matriz: list)-> int:
    '''
    Calcula la constanste mágica de la matriz cuadrada ingresada.

    Parametros: "matriz"-> matriz a calcular la constante.

    Retorno: El resultado luego de calcular el valor de la constante.
    '''
    m = (len(matriz)*(len(matriz)**2 + 1))/2

    return m


def comparar_sumas_matriz_magica(matriz: list)-> bool:
    '''
    Compara la suma de los elementos de la matriz.

    Parametros: "matriz" ->  matriz con elementos a comparar.
                

    Retorno: True -> si es mágico.
             False -> si no es mágico.
    '''
    m = calcular_constante_magica(matriz)
    bandera = False

    if validar_fila_magica(matriz,m) and validar_columna_magica(matriz,m) and validar_diagonal_magica(matriz,m):
        bandera = True

    return bandera


def validar_fila_magica(matriz: list, 
                        m: int)-> bool:
    '''
    Valida la suma de cada fila de la matriz.

    Parametros: "matriz"-> matriz con números a sumar.
                "m" -> valor de referencia.

    Retorno: True -> si se cumple la propiedad de matriz mágica.
             False -> en caso de que no se cumpla.
    '''
    #Suma cada fila.
    for i in range(len(matriz)):
        acumulador = 0
        #Recorre los números de la fila "i".
        for j in range(len(matriz[i])):
            acumulador += matriz[i][j]

        #Valida que se cumpla la propiedad de matriz mágica.
        if acumulador != m: 
            return False
        
    return True

def validar_columna_magica(matriz: list,
                           m: int)-> bool:
    '''
    Valida la suma de cada columna de la matriz.

    Parametros: "matriz"-> matriz con números a sumar.
                "m" -> valor de referencia.

    Retorno: True -> si se cumple la propiedad de matriz mágica.
             False -> en caso de que no se cumpla.
    '''
    #Suma cada columna.
    for i in range(len(matriz[0])):
        acumulador = 0
        #Recorre los números de la columna "i".
        for j in range(len(matriz)):
            acumulador += matriz[j][i]

        #Valida que se cumpla la propiedad de matriz mágica.
        if acumulador != m: 
            return False
        
    return True


def validar_diagonal_magica(matriz: list, constante_magica: int)-> bool:
    '''
    Valida que la diagonal de la matriz cuadrada sea mágica.

    Parametro: "matriz" -> matriz a validar.
               "constante_mágica" -> valor de la constante.

    Retorno: True si es mágico.
             False en caso contrario.
    '''
    diagonal_1 = 0
    diagonal_2 = 0

    #Recorre la diagonal de arriba hacia abajo.
    for i in range(len(matriz)):
        diagonal_1 += matriz[i][i]

    if diagonal_1 == constante_magica:
        indice = len(matriz) - 1

        for i in range(len(matriz)):
            diagonal_2 += matriz[indice][i]
            indice -= 1
    else:
        return False
    
    if diagonal_2 == constante_magica:
        return True


def validar_matriz_magica(matriz):
    '''
    compara que la suma de los números en cada fila, cada columna y cada diagonal principal es la misma

    Parametro: "matriz" -> matriz a validar.

    return: True si se cumple lo anteriormente dicho
            False si no se cumple
    '''
    m = calcular_constante_magica(matriz)

    if validar_fila_magica(matriz,m) and validar_columna_magica(matriz, m) and validar_diagonal_magica(matriz, m):
        return True
    
    return False


def cargar_secuencial_random(matriz: list,
                             limite: int):
    '''
    Carga secuencialmente los números a la matriz hasta "limite"
    '''
    for i in range(len(matriz)):

        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(1,limite)
    
    return matriz
