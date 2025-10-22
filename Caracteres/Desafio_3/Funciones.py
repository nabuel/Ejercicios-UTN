def mostrar_array(array: list)-> None:
    '''
    Muestra todos los elementos del array por consola.
    '''
    for i in range(len(array)):
        print(array[i], end="")


def recortar_lista(lista: list,
                   valor = False)-> list:
    '''
    Recorta la lista hasta el valor dado.

    Retorno: la lista recortada.
    '''
    indice_corte = len(lista) - 1
    for i in range(len(lista)):
        if lista[i] == valor:
            indice_corte = i
            break
    
    lista_retorno = [False] * indice_corte

    for j in range(len(lista)):
        if lista[j] == valor:
            break
        lista_retorno[j] = lista[j]
        
    return lista_retorno

def validar_vocal(letra: str)-> bool:
    '''
    Valida si la letra es una vocal.

    Retorno: True si es vocal.
             False si no lo es.
    '''
    match ord(letra):
        case 65 | 97:
            return True
        case 69 | 101:
            return True
        case 73 | 105:
            return True
        case 79 | 111:
            return True
        case 85 | 117:
            return True
        case _:
            return False

def validar_consonante(letra: str)-> bool:
    '''
    Valida si la letra es una consonante.
    '''
    if ord(letra) > 64 and ord(letra) < 91:
        if not validar_vocal(letra):
            return True
    elif ord(letra) > 96 and ord(letra) < 123:
        if not validar_vocal(letra):
            return True
    else:
        return False
    

def validar_numero(numero: str)-> bool:
    '''
    Válida si el caracter ingresado es un número entero positivo.

    Retorno: True si es un número entero positivo.  
             False si no lo es.
    '''
    if ord(numero) >57 or ord(numero)< 48:
        return False
    else:
        return True