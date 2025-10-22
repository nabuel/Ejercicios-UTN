def ordenar_array(array: list,
                  descendente = False)-> list:
    '''
    Ordena de forma ascendente el array. Si la bandera es True ordena el array en orden descendente.

    Retorno: la lista ordenada.
    '''
    if descendente:
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                numero = array[j]
                if numero < array[j + 1]:
                    array[j] = array[j + 1]
                    array[j + 1] = numero
    else:
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                numero = array[j]
                if numero > array[j + 1]:
                    array[j] = array[j + 1]
                    array[j + 1] = numero
    
    return array


lista = [5,4,3,2,1]
lista_retorno = ordenar_array(lista,True)
print(lista_retorno)

def intercalar_vectores(vector_1: list,
                        vector_2: list,
                        descendente = False)-> list:
    '''
    Ordena de forma ascendente los dos vectores recibidos en un único vector. En caso de que "descendente" sea True la ordena de forma descendente.

    Parametros: "vector_1","vector_2" -> lista de números enteros ordenados.

    Retorno: una lista ordenada en el sentido indicado. 
    '''
    longitud = len(vector_1) + len(vector_2)
    vector_retorno = [False] * longitud

    #Cargo el vector de retorno con los elementos del primer array.
    for i in range(len(vector_1)):
        vector_retorno[i] = vector_1[i]
        indice = i + 1
    
    #Cargo el vector de retorno con los elementos del segundo array.
    for j in range(len(vector_2)):
        vector_retorno[indice] = vector_2[j]
        indice += 1
    
    vector_retorno = ordenar_array(vector_retorno, descendente)
    return vector_retorno


def ordenar_negativos_positivos(vector: list)-> list:
    '''
    Ordena los números negativos del vector en orden decreciente y los positivos en orden creciente.

    Retorno: la lista con los elementos ordenados.
    '''
    for i in range(len(vector)):
        for j in range(len(vector)-1-i):
            numero = vector[j]
            if numero >= 0 and numero > vector[j + 1]:
                vector[j] = vector[j + 1]
                vector[j + 1] = numero
            elif numero < 0 and numero < vector[j + 1]:
                vector[j] = vector[j + 1]
                vector[j + 1] = numero
    return vector

lista_2 = [-5,4,-3,2,-1,5,-4,3,-2,1,0]
print(ordenar_negativos_positivos(lista_2))