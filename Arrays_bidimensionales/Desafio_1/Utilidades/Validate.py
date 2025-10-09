def validate_number(numero: int|float,
                    minimo: int|float,
                    maximo: int|float,
                    ) -> bool:
    '''
    Valida si el valor dado es un número entero.

    Parametros: "numero" -> número a validar.
                "minimo" -> minimo que se contempla en el rango.
                "maximo" -> maximo que se contempla en el rango.
                

    Si "numero" está en el rango entre "minimo" y "maximo" inclusive es retornado. En caso de que sea un valor inválido se le solicita al usuario que lo vuelva a escribir un número válido.
    '''         
    return (numero <= maximo) and (numero >= minimo)

def validate_length(texto: str,
                    longitud: int,)-> str:
    '''
    Valida que la cadena de texto ingresada sea de la longitud especificada. En caso de el texto no sea válido, se solicita que lo escriba de nuevo.

    Parametros: "texto" -> cadena de texto a validar.
                "longitud" -> cantidad de caracteres de la cadena de texto.
    
    Si la cantidad de caracteres de "texto" es igual a "longitud" se retorna "texto". En caso contrario se solicita al usuario que vuelva a escribir un texto válido.        
    '''
    return len(texto) <= longitud 