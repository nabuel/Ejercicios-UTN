from .Input import *
from .Validate import *

#Punto 1.

def crear_array(longitud: int)->int:
    '''
    Crea un array de números con la longitud "longitud".

    Parametro: "longitud" -> es la longitud de la array.

    Retorno: una array.
    '''
    array = [False] * longitud

    return array

#Punto 2.

def crear_array_personalizada() -> int:
    '''
    Crea un array con la cantidad de números que quiera ingresar el usuario.

    Retorna la array creada.
    '''

    longitud = get_int(1,100,"Ingrese la cantidad de números que quiere ingresar: ", "número fuera de los límites.")
    array = crear_array(longitud)
    for i in range(len(array)):
        array[i] = get_int(-10000,10000,"Ingrese un número: ","número fuera de los límites.")

    return array

#Punto 3.

def calcular_promedio_lista(lista: list)->float:
    '''
    Calcula el promedio entre los números de la lista.

    Parametros: "lista" -> lista con números.

    Retorna el promedio calculado.
    '''
    suma = 0
    for i in lista:
        suma += i
    promedio = suma / len(lista)

    return promedio

#Punto 4

def calcular_promedio_positivos_en_lista(lista: list)->float:
    '''
    Calcula el promedio entre los números positivos de la lista.

    Parametros: "lista" -> lista con números.

    Retorna el promedio calculado.
    '''
    suma = 0
    contador = 0
    
    for i in lista:
        if i >= 0:
            suma += i
            contador += 1
    promedio = suma / contador

    return promedio

#Punto 5.

def calcular_producto_de_lista(lista: list)->float:
    '''
    Calcula el producto de todos los números dentro de la lista "lista".

    Parametros: "lista"-> lista que contiene números.

    Retorno producto calculado.
    '''
    producto = 1
    for i in lista:
        producto *= i
    
    return producto

#Punto 6. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

