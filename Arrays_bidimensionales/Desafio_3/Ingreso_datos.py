def get_int(mensaje: str)->int:
    '''
    Consigue un número entero.
    '''
    numero = input(mensaje)
    numero = validar_numero(numero)
    while type(numero) != int:
        numero = input(mensaje)
        numero = validar_numero(numero)

    return numero

def validar_numero(caracter: str)->int|None:
    '''
    Válida que el caracter ingresado sea un número.
    '''
    if ord(caracter) > 57 or ord(caracter) < 48:
        print("Ingrese un número.")
    else:
        return int(caracter)