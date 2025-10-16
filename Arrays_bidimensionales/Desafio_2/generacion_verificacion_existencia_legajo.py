import random


def crear_legajos(cantidad_legajos: int) -> list:
    '''
    Crea una lista con el número de legajo de los choferes.

    Parametro: "cantidad_legajos" -> cantidad de legajos que se van a generar.

    Retorno: la lista con los legajos cargados.
    '''

    legajos = [False] * cantidad_legajos

    while validar_repetidos(legajos):
        for i in range(len(legajos)):
            legajos[i] = random.randint(10000, 99999)

    return legajos

def validar_numero(lista: list, numero: int|float) -> bool:
    '''
    Valida si "numero" está en "lista".

    Parametros: "lista" -> lista con números.
                "número" -> número a buscar
    
    Retorno: True en caso de que se encuentre
             False en caso contrario.
    '''

    for i in range(len(lista)):
        if numero == lista[i]:
            return True
    
    return False


def validar_repetidos(lista: list)-> bool:
    '''
    Valida si hay un número repetido en la lista.

    Parametro: "lista" -> lista de números.

    Retorno: True -> si hay un número repetido.
             False -> en caso contrario.
    '''
    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                contador += 1
        if contador > 1:
            return True
    return False