def validar_colectivo(linea: int,
                      coche: int,
                      registro: list)-> bool:
    '''
    Válida que exista el colectivo en la línea "linea" y coche "coche" en los archivos de la empresa "empresa".

    Parametros: "linea" -> línea del colectivo.
                "coche" -> número del coche.
                "empresa" -> registro de colectivos.
    
    Retorno: True en caso de que exista.
             False en caso contrario.
    '''

    return validar_linea(linea, registro) and validar_coche(coche, registro)

def validar_linea(linea: int, registro: list)-> bool:
    '''
    Válida que exista la línea en la empresa de colectivos.

    Parametros: "linea" -> línea del colectivo.
                "empresa" -> registro de colectivos.
    
    Retorno: True si existe la línea.
             False en caso contrario.
    '''
    if linea <= 0 or linea > len(registro):
        return False
    return True

def validar_coche(coche: int, registro: list) ->bool:
    '''
    Válida que exista el coche en el registro de la empresa de colectivos.

    Parametros: "coche" -> coche del colectivo.
                "registro" -> registro de colectivos.
    
    Retorno: True si existe la coche.
             False en caso contrario.
    '''

    if coche <= 0 or coche > len(registro[0]):
        return False
    return True

