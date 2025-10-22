import Ingreso_datos, random, Verificaciones
def crear_matriz(filas: int,
                 columnas: int,
                 valor = False)-> list:
    '''
    Crea una matriz.
    '''
    matriz = []

    for _ in range(filas):
        fila = [valor] * columnas 
        matriz += [fila]

    return matriz


def cargar_matriz_enteros_secuencial(matriz: list)-> list:
    '''
    Carga secuencialmente la matriz con números enteros positivos.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = Ingreso_datos.get_int("Ingrese un número entero positivo: ")
            matriz[i][j] = numero
    return matriz

def cargar_matriz_random(matriz: list, 
                         limite: int) -> list:
    '''
    Carga la matriz con números enteros positivos aleatorios.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(0, limite)

def contar_secuencias_pares_matriz(matriz: list)-> int:
    '''
    Cuenta la cantidad de secuencias pares hay en la matriz.
    '''
    contador = 0
    for i in range(len(matriz)):
        if Verificaciones.verificar_secuencia_pares_lista(matriz[i]):
            contador += 1
    
    return contador

def buscar_secuencia_corta_pares_matriz(matriz:list)->list|None:
    '''
    Busca la secuencia más corta de números pares.

    Retorno: la secuencia más corta de números pares consecutivos. 
            None si no existe una secuencia de números pares consecutivos.
    '''
    secuencia_retorno = [] * len(matriz[i])
    
    
    for i in range(len(matriz)):
        secuencia_actual = buscar_secuencia_corta_pares_lista(matriz[i])
        if len(secuencia_retorno) >= secuencia_actual:
            secuencia_retorno = secuencia_actual
    
    
    return secuencia_retorno

def buscar_secuencia_corta_pares_lista(lista: list)-> list:
    '''
    Busca la secuencia más corta de la lista.
    '''

    secuencia_retorno = lista
    indice_inicio = 0
    indice_final = 0
    
    for i in range(len(lista) - 1):
        
        numero = lista[i]
        if Verificaciones.definir_par(lista[i]):
            indice_inicio = i
            if numero + 2 == lista[i + 1]: 
                indice_final = i + 1
    
    
    secuencia_retorno = recortar_lista(secuencia_retorno, indice_inicio, indice_final)

    return secuencia_retorno


def recortar_lista(lista: list,
                   indice_inicio = 0,
                   indice_final = 1)-> list:
    '''
    Recorta la lista  desde el indice de inicio hasta el indice de final.
    '''
    lista_retorno = [False] * (indice_final + 1)
    indice = 0
    for i in range(indice_inicio, indice_final + 1):
        lista_retorno[indice] = lista[i]
        indice +=1
    
    return lista_retorno



lista = [0,2,3,4,5,6]

print(buscar_secuencia_corta_pares_lista(lista))