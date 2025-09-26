def definir_par_o_impar(numero: int) -> bool:
    '''
    Define si el número ingresado es par o impar.

    Parametros: "numero" -> número a definir si es par o impar.

    Retorno:    True en caso de que sea par.
                False en caso de ser impar.
    '''
    resto = numero % 2
    es_par = False

    if resto == 0:
        es_par = True
    
    return es_par


def mostrar_menu() -> None:
    '''
    Muestra el menu con las funciones disponibles

    Retorno: None.
    '''
    print("---------------------")
    print("1- Cantidad de positivos y negativos.")
    print("2- Suma de los números pares.")
    print("3- Mayor número impar.")
    print("4- Listar los números ingresados.")
    print("5- Listar los números pares.")
    print("6- Listar los números en posiciones impares.")
    print("7- Salir del programa.")
    print("---------------------")
