from .Validate import validate_number
from .arrays import crear_array
from .Especificas import *


def ingresar_datos()-> list:
    '''
    El usuario puede ingresar 10 números enteros desde -1000 al 1000.

    Retorna un lista con los 10 números ingresados.
    '''
    contador = 0
    lista_numeros = crear_array(10)
    while contador != 10:
        numero = int(input("Ingrese un número entero: "))
        if validate_number(numero, -1000,1000):
            lista_numeros[contador] = numero
            contador += 1
        else:
            print("Número fuera de limites. Por favor escriba un número dentro de un rango de -1000 y 1000.")
    
    return lista_numeros

def contar_positivos_negativos(lista: list)->None:
    '''
    Cuenta la cantidad de números positivos, negativos de la lista y los muestra por pantalla.

    Parametros: "lista" -> lista de números.

    Retorna: None.
    '''
    positivos = 0
    negativos = 0

    for i in range(len(lista)):
        if lista[i] >= 0:
            positivos += 1
        else:
            negativos += 1
    
    print(f"Cantidad de números positivos: {positivos}\nCantidad de números negativos: {negativos}")

def sumar_numeros_pares(lista: list)->None:
    '''
    Suma los números pares de la lista y los muestra por pantalla.

    Parametros: "lista" -> lista de números.

    Retorna: None.
    '''
    resultado = 0
    for i in range(len(lista)):
        if definir_par_o_impar(lista[i]):
            resultado += lista[i]
    
    print(f"El resultado de sumar los pares es {resultado}")

def calcular_mayor_impar(lista: list)->int:
    '''
    Busca el mayor número impar y lo muestra por pantalla.

    Parametros: "lista" -> lista de números.

    Retorno: None.
    '''
    mayor_impar = 0

    for i in range(len(lista)):
        if definir_par_o_impar(lista[i]) == False and lista[i] > mayor_impar:
            mayor_impar = lista[i]
        #Esto sirve si en la lista todos los números son negativos.
        elif definir_par_o_impar(lista[i]) == False and i == mayor_impar:
            mayor_impar = lista[i]
    print(f"El impar más grande es {mayor_impar}")

def listar_pares(lista: list)->None:
    '''
    Lista los números pares de "lista" mostrandolos por pantalla.

    Parametros: "lista" -> lista de números.

    Retorno: None.
    '''

    for i in range(len(lista)):
        if definir_par_o_impar(lista[i]):
            print(lista[i])

def listar_numeros(lista: list)-> None:
    '''
    Muestra por consola cada número ingreaso en orden de ingreso.

    Parametros: "lista" -> lista de números.

    Retorno: None.
    '''

    for i in range(len(lista)):
        print(lista[i])

def listar_numeros_posicion_impar(lista: list)-> None:
    '''
    Muestra por pantalla todos los números que estén en posiciones impares.

    Parametros: "lista" -> lista con números.

    Retorno: None.
    '''
    for i in range(len(lista)):
        if definir_par_o_impar(i) == False:
            print(lista[i])



