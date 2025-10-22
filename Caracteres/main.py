#Punto 1.
def contar_vocales(palabra: str)-> None:
    '''
    Cuenta la cantidad de vocales que hay en la palabra ingresada.

    Retorno: La cantidad de vocales.
    '''
    cantidad_a = 0
    cantidad_e = 0
    cantidad_i = 0
    cantidad_o = 0
    cantidad_u = 0
    
    for i in range(len(palabra)):
        valor_letra = ord(palabra[i])
        match valor_letra:
            case 65 | 97:
                cantidad_a += 1
            case 69 | 101:
                cantidad_e += 1
            case 73 | 105:
                cantidad_i += 1
            case 79 | 111:
                cantidad_o += 1
            case 85 | 117:
                cantidad_u += 1
    
    matriz = [['"a": ', cantidad_a],
              ['"e": ', cantidad_e],
              ['"i": ', cantidad_i],
              ['"o": ', cantidad_o],
              ['"u": ', cantidad_u]]
    
    print(matriz)

#Punto 2.
def buscar_indice_letra(palabra: str,
                        letra: str)-> int:
    '''
    Busca el índice de la primer aparición de la letra.
    
    Retorno: El índice de la letra. En caso de que no esté se devuelve -1
    '''
    for i in range(len(palabra)):
        if ord(palabra[i]) == ord(letra):
            return i
        elif ord(palabra[i]) == ord(letra) + 32:
            return i
        elif ord(palabra[i]) == ord(letra) - 32:
            return i
    
    return -1

#Punto 3.
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
    
#Punto 4.
def mostrar_array(array: list)-> None:
    '''
    Muestra todos los elementos del array por consola.
    '''
    for i in range(len(array)):
        print(array[i], end="")


def suprimir_repetidos(palabra: str)-> None:
    '''
    Suprime las letras repetidas consecutivas de la palabra.

    Retorno: La palabra sin las letras repetidas.
    '''
    palabra_retorno = [False] * len(palabra)
    indice = 0
    ultima_letra = "1"
    for i in range(len(palabra)):
        if ord(palabra[i]) == ord(ultima_letra):
            pass
        elif ord(palabra[i]) == ord(ultima_letra) + 32:
            pass
        elif ord(palabra[i]) == ord(ultima_letra) - 32:
            pass
        else:
            palabra_retorno[indice] = palabra[i] 
            indice += 1
            ultima_letra = palabra[i]
    
    palabra_retorno = recortar_lista(palabra_retorno)

    mostrar_array(palabra_retorno)

def recortar_lista(lista: list,
                   valor = False)-> list:
    '''
    Recorta la lista hasta el valor dado.

    Retorno: la lista recortada.
    '''
    indice_corte = len(lista)
    for i in range(len(lista)):
        if lista[i] == valor:
            indice_corte = i
            break

    lista_retorno = [False] * (indice_corte)

    for j in range(len(lista_retorno)):
        if lista[j] != valor:
            lista_retorno[j] = lista[j]
    
    return lista_retorno


#Punto 5.

def suprimir_vocales(palabra: str)-> None:
    '''
    suprime las vocales de la palabra.

    Retorno: la palabra sin las vocales.
    '''
    palabra_retorno = [False] * len(palabra)
    indice = 0

    for i in range(len(palabra)):
        if not validar_vocal(palabra[i]):
            palabra_retorno[indice] = palabra[i]
            indice += 1
    
    palabra_retorno = recortar_lista(palabra_retorno)

    mostrar_array(palabra_retorno)


def validar_vocal(letra: str)-> bool:
    '''
    Valida que la letra sea una vocal.

    Retorno: True si lo es.
             False en caso de que no lo sea.
    '''
    bandera = False
    match ord(letra):
        case 65 | 97:
            bandera = True
        case 69 | 101:
            bandera = True
        case 73 | 105:
            bandera = True
        case 79 | 111:
            bandera = True
        case 85 | 117:
            bandera = True
    
    return bandera



def contar_subcadena(frase: str,
                     subcadena: str)-> int:
    '''
    Cuenta la cantidad de veces que aparece la subcadena indicada.

    Retorno: la cantidad de veces que aparece la subcadena.
    '''
    contador_apariciones = 0
    indice = 0

    for i in range(len(frase)):
        if indice == len(subcadena):
            contador_apariciones += 1
            indice = 0

        if validar_mismo_caracter(frase[i], subcadena[indice]):
            indice += 1
        else:
            indice = 0

    return contador_apariciones


print(contar_subcadena("El panpan del panadero", "Pan"))
