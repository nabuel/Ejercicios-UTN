from Utilidades import Validate

def get_int(minimo: int,
            maximo: int,
            mensaje: str,
            mensaje_error: str,
            reintentos: int)-> int | None:
    '''
    Solicita un número entero.

    Parametros: "minimo" -> minimo que se contempla en el rango.
                "maximo" -> maximo que se contempla en el rango.
                "mensaje" -> mensaje que se imprime para pedir un número al usuario.
                "mensaje_error" -> mensaje que se muestra por pantalla en caso de que el dato ingresado sea inválido.
                "reintentos" -> cantidad de reintentos que tiene. 

    Retorna un número entero validado.
    '''
    print(mensaje)
    while reintentos != 0:
        numero = int(input("Ingrese un número: "))
        if Validate.validate_number(numero, minimo, maximo):
            return numero
        else:
            print(mensaje_error)
            reintentos -= 1
    return None
        
    

def get_float(minimo: float,
              maximo: float,
              mensaje: str,
              mensaje_error: str) -> float|None :
    '''
    Solicita un número decimal.

    Parametros: "minimo" -> minimo que se contempla en el rango.
                "maximo" -> maximo que se contempla en el rango.
                "mensaje" -> mensaje que se imprime para pedir un número al usuario.
                "mensaje_error" -> mensaje que se muestra por pantalla en caso de que el dato ingresado sea inválido.

    Retorna un número decimal validado.
    '''
    print(mensaje)
    while reintentos != 0:
        numero = float(input("Ingrese un número: "))
        if Validate.validate_number(numero, minimo, maximo):
            return numero
        else:
            print(mensaje_error)
            reintentos -= 1
    return None
    

def get_string(longitud: int,
               mensaje: str,
               mensaje_error: str)->str|None:
    '''
    Solicita una cadena de texto.

    Parametros: "longitud" -> cantidad de caracteres de la cadena de texto.
                "mensaje" -> mensaje que se imprime para pedir el texto al usuario.
                "mensaje_error" -> mensaje que se muestra por pantalla en caso de que el texto ingresado sea inválido.

    Retorna el texto validado.
    '''
    print(mensaje)
    texto = str(input("Escriba a continuación: "))
    if Validate.validate_length(texto, longitud):
        return texto
    else:
        print(mensaje_error)
        return None
    
    