def castear_numero(valor_ingresado: str, mensaje_error = "")-> int|None:
    '''
    castea un texto a un número.

    Parametros: "valor_ingresado" -> es el valor ingresado.
                "mensaje_error" -> mensaje que se muestra por pantalla en caso de que no sea un número.
    '''
    bandera = True
    #Verifica que no haya una letra.
    for i in range(len(valor_ingresado)):
        
        if ord(valor_ingresado[i]) > 57 or ord(valor_ingresado[i]) < 48:
            bandera = False
            break
    
    if bandera:   
        return int(valor_ingresado)
    else:
        print(mensaje_error)



def get_int(mensaje: str, mensaje_error: str)-> int:
    '''
    Consigue un número entero positivo.

    Parametros: "mensaje" -> mensaje que se le muestra al usuario para que ingrese un número.
                "mensaje_error" -> mensaje que se le muestra al usuario en caso de que ingrese un caracter que no sea número. 
    '''
    numero = input(mensaje)
    numero_casteado = castear_numero(numero, mensaje_error)

    while type(numero_casteado) != int:
        numero = input(mensaje)
        numero_casteado = castear_numero(numero, mensaje_error)

    return numero_casteado

def calcular_cantidad_fiestas(matriz: list, salon: list)-> None:
    '''
    Muestra por pantalla la cantidad de fiestas realizadas en cada salón.

    Parametros: "matriz" -> registro donde está guardada la cantidad de fiestas realizadas.
                "salones" -> localidad de los salones de fiesta.
    '''
    fiestas_celebradas = 0
    for i in range(len(matriz)):
        fiestas_celebradas = sumar_numeros_array(matriz[i])
        print(f"La cantidad de fiestas celebradas en el salón de {salon[i]} es de: {fiestas_celebradas}")
        print()


def sumar_numeros_array(lista: list)-> int|float:
    '''
    suma los números del array.

    Parametros: "lista" -> lista a la que se le suman los números.

    Retorno: la suma de los elementos de la lista.
    '''
    resultado = 0

    for i in range(len(lista)):
        resultado += lista[i]
    
    return resultado

def buscar_evento_mas_realizado(matriz: list, 
                                salon: list,
                                evento: list)-> None:
    '''
    Busca el evento más realizado en cada salón.

    Parametro: "matriz" -> matriz a buscar cada salón.
               "salon" -> localidad de los salones de fiesta.
               "evento" -> tipos de eventos.
    '''

    for i in range(len(matriz)):
        evento_mayor = buscar_mayor_array(matriz[i])
        print(f"El evento más realizado del salón de {salon[i]} son {evento[evento_mayor]}")
        print()


def buscar_mayor_array(lista: list)-> int:
    '''
    Busca el número mayor de la lista.

    Parametro: "lista" -> lista a recorrer.

    Retorno: Devuelve el índice del número mayor de la lista.
    '''
    posicion_mayor = 0
    for i in range(len(lista)):
        if lista[posicion_mayor] < lista[i]:
            posicion_mayor = i
    
    return posicion_mayor

#Punto 4.
def calcular_recaudacion_por_salon(matriz: list,
                                   salon: list,
                                   valor_eventos: list)-> None:
    '''
    Calcula la recaudación de cada salón.

    Parametros: "matriz" -> matriz a buscar cada salón.
                "salon" -> localidad de los salones de fiesta.
                "valor_eventos" -> costo de cada evento.
    '''
    recaudacion = 0
    for i in range(len(matriz)):
        recaudacion = calcular_recaudacion_del_salon(matriz[i], valor_eventos)
        print(f"La recaudación del salón de {salon[i]} es de {recaudacion}$.")

def calcular_recaudacion_del_salon(salon: list,
                                   valor_eventos: list)-> int:
    '''
    Calcula la recaudación del salón.

    Retorno: la recaudación del salón.
    '''
    recaudacion = 0
    for i in range(len(salon)):
        recaudacion += salon[i] * valor_eventos[i]
    
    return recaudacion

#Punto 6.
def calcular_porcentaje_bodas_del_salon(salon: list)-> int|float:
    '''
    Calcula el porcentaje de bodas de oro realizadas en el salón.

    Retorno: El porcentaje de bodas de oro realizadas.
    '''
    cantidad = sumar_numeros_array(salon)
    porcentaje = (salon[3] * 100) / cantidad
    return porcentaje



def ordenar_lista_mayor_menor(lista: list)-> list:
    '''
    Ordena la lista de mayor a menor.

    Retorna la lista ordenada.
    '''
    reemplazado = 0
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):

            if lista[j] < lista[j + 1]:
                reemplazado = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = reemplazado

    return lista
