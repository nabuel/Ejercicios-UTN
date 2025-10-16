def get_int(mensaje: str,
            mensaje_error = None)-> int:
    '''
    Solicita un número entero.

    Parametros: "mensaje" -> mensaje que se imprime para pedir un número al usuario.
                "mensaje_error" -> mensaje que se muestra por pantalla en caso de que el dato ingresado sea inválido.

    Retorna un número entero.
    '''
    numero = input(mensaje)
    numero_casteado = castear_numero_entero(numero, mensaje_error)
    
    while type(numero_casteado) != int:
        numero = input(mensaje)
        numero_casteado = castear_numero_entero(numero, mensaje_error)

    return numero_casteado

def castear_numero_entero(numero: str,
                          mensaje_error = None) -> int|None:
    '''
    Castea el número ingresado a entero.

    Parametros: "numero" -> número a castear.

    Retorno: retorna el número casteado.
             None en caso contrario.
    ''' 
    bandera = True
    
    for i in range(len(numero)):
        if ord(numero[i]) > 57 or ord(numero[i]) < 48:
            bandera = False
            break
    
    if bandera:
        return int(numero)
    elif type(mensaje_error) != None:
            print(mensaje_error)
            print("")
    else:
        return None
