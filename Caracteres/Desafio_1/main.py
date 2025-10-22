#Punto 1.
def validar_cadena_alfabetica(texto: str)->bool:
    '''
    Define si la cadena está compuesta por mayúsculas y minúsculas.

    Retorno: True si está compuesta por mayúsculas y minúsculas.
    '''
    bandera = True
    for i in range(len(texto)):
        if not validar_mayuscula(texto[i]) and not validar_minuscula(texto[i]):
            bandera = False
            break
    
    return bandera

def validar_mayuscula(letra: str)-> bool:
    '''
    Define si la letra es mayúscula.

    Retorno: True si es mayúscula.
             False si no lo es.
    '''
    if ord(letra) < 65 or ord(letra) > 90:
        return False
    else:
        return True

def validar_minuscula(letra: str)-> bool:
    '''
    Define si la letra es minúscula.

    Retorno: True si es minúscula.
             False si no lo es.
    '''

    if ord(letra) < 97 or ord(letra) > 122:
        return False
    else:
        return True

#Punto 2.
def validar_numero_entero(numero: str)-> bool:
    '''
    Valida si el número ingresado es un número entero.

    Retorno: True si es válido.
             False si no lo es.
    '''
    bandera = True

    match ord(numero[0]):
        case 43 | 45:
            for i in range(1,len(numero)):
                if ord(numero[i]) < 48 or ord(numero[i]) > 57:
                    bandera = False
                    break
        case _:
            for i in range(len(numero)):
                if ord(numero[i]) < 48 or ord(numero[i]) > 57:
                    bandera = False
                    break
    
    return bandera

#Punto 3.
def validar_numero_decimal(numero: str)-> bool:
    '''
    Determina la cadena representa un número decimal válido con un solo punto decima.

    Retorno: True si es válido.
             False si no lo es.
    '''
    bandera = True
    contador = 0
    
    match ord(numero[0]):
        case 43 | 45:
            for i in range(1,len(numero)):
                if contador > 1:
                    bandera = False
                    break
                elif i >= 1 and (ord(numero[i]) == 46 or ord(numero[i]) == 44):
                    contador += 1
                elif ord(numero[i]) < 48 or ord(numero[i]) > 57:
                    bandera = False
                    break
        case _:
            for i in range(len(numero)):
                if contador > 1:
                    bandera = False
                    break
                elif i >= 1 and (ord(numero[i]) == 46 or ord(numero[i]) == 44):
                    contador += 1
                elif ord(numero[i]) < 48 or ord(numero[i]) > 57:
                    bandera = False
                    break
    
    return bandera

#Punto 4.
def validar_clave_segura(clave: str)-> bool:
    '''
    Válida si la contraseña es segura.

    Retorno: True si es válida.
             False si no lo es.
    '''
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    if len(clave) >= 8:
        for i in range(len(clave)):
            if validar_mayuscula(clave[i]):
                tiene_mayuscula = True
            elif validar_minuscula(clave[i]):
                tiene_minuscula = True
            elif validar_numero_entero(clave[i]):
                tiene_numero = True
    
        if tiene_mayuscula and tiene_minuscula and tiene_numero:
            return True
        else:
            return False
    else:
        return False


#Punto 5.
def validar_palindromo(texto: str)-> bool:
    '''
    Valida si la palabra ingresada es un palindromo.

    Retorno: True si lo es.
             False en caso de que no lo sea.
    '''
    indice_inverso = len(texto) - 1
    for i in range(len(texto)):
        if validar_mismo_caracter(texto[i], texto[indice_inverso]):
            indice_inverso -= 1
        else:
            return False
    
    return True


def validar_mismo_caracter(caracter: str,
                           caracter_2: str) -> bool:
    '''
    Valida si el caracter es el mismo, tanto en forma mayúscula o minúscula.

    Retorno: True en caso de que sea el mismo caracter.
             False en caso contrario.
    '''
    if ord(caracter) == ord(caracter_2):
        return True
    elif ord(caracter) == (ord(caracter_2) - 32):
        return True
    elif ord(caracter) == (ord(caracter_2) + 32):
        return True
    else:
        return False
    

#Punto 6.
def validar_correo(correo: str)-> bool:
    '''
    Valida si el correo ingresado es válido.

    Retorno: True si es válido.
             False si no lo es.
    '''
    contador_arroba = 0
    contador_punto = 0
    caracteres = 0

    for i in range(len(correo)):
        
        if ord(correo[i])== 64 and caracteres > 0:
            contador_arroba += 1
            caracteres = 0
        elif ord(correo[i]) == 46 and contador_arroba > 0 and caracteres > 0:
            contador_punto += 1
            caracteres = 0
        elif contador_arroba > 1:
            return False
        caracteres += 1
    if contador_arroba > 0 and contador_punto > 0 and caracteres >= 2:
        return True
    else:
        return False

#Punto 7.

def contar_vocales_consonantes(texto: str)-> None:
    '''
    Cuenta y muestra por connsola la cantidad de vocales y consonantes del texto ingresado.
    '''
    vocales = 0
    consonantes = 0

    for i in range(len(texto)):
        if validar_vocal(texto[i]):
            vocales += 1
        elif validar_consonante(texto[i]):
            consonantes += 1
    
    print(f"Cantidad de vocales: {vocales}\nCantidad de consonantes: {consonantes}")

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
    Valida si la letra es una vocal.
    '''
    if ord(letra) > 64 and ord(letra) < 91:
        if not validar_vocal(letra):
            return True
    elif ord(letra) > 96 and ord(letra) < 123:
        if not validar_vocal(letra):
            return True
    else:
        return False


def validar_numero_telefono(telefono: str)-> bool:
    '''
    Válida si el número de telefono es válido.

    Retorno: True si es válido.
             False si no lo es.
    '''

    if len(telefono) != 10:
        return False
    
    if ord(telefono[0]) == 48 and (ord(telefono[1]) != 50 and ord(telefono[1]) != 57):
        return False

    for i in range(len(telefono)):
        if not validar_numero_entero(telefono[i]):
            return False
    
    return True

print(validar_numero_telefono("0234567893"))
