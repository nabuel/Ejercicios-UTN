def verificar_secuencias_pares_matriz(matriz: list)-> bool:
    '''
    Verifica si en la matriz hay alguna secuencia de números pares.

    Retorno: True en casa de que haya.
             False en caso contrario.
    '''
    contador = 0
    for i in range(len(matriz)):
        if verificar_secuencia_pares_lista(matriz[i]):
            contador += 1
    
    if contador != 0:
        return True
    else:
        return False

def verificar_secuencia_pares_lista(lista: list)-> bool:
    '''
    Verifica si la lista es una secuencia de números pares.

    Retorno: True en caso de que lo sea.
             False en caso contrario.
    '''
    contador = 0
    
    for i in range(len(lista) - 1):
        numero = lista[i]
        if definir_par(numero):
            if numero + 2 == lista[i + 1]:
                contador += 1
        else:
            break
    
    if contador == len(lista) - 1:
        return True
    else:
        return False

def definir_par(numero: int)-> bool:
    '''
    Define si el número es par.

    Retorno: True si es par.
             False si es impar.
    '''
    resto = numero % 2

    if resto == 0:
        return True
    else:
        return False

print(len([]))