
def buscar_subcadena(cadena_1: str,
                     subcadena: str)-> bool:
    '''
    Compara ambas cadenas para saber si son iguales. Diferencia entre mayúsculas y minúsculas.

    Retorno: True si son iguales.
             False si no lo son.
    '''
    indice = 0
    if len(cadena_1) < len(subcadena):
        return False
    
    for i in range(len(cadena_1)):
        if indice == len(subcadena):
            return True
        
        if ord(cadena_1[i]) == ord(subcadena[indice]):
            indice += 1
        else:
            indice = 0
    
    return False