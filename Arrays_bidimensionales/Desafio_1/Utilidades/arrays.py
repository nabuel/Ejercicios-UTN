from Utilidades import Input


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

    longitud = Input.get_int(1,100,"Ingrese la cantidad de números que quiere ingresar: ", "número fuera de los límites.")
    array = crear_array(longitud)
    for i in range(len(array)):
        array[i] = Input.get_int(-10000,10000,"Ingrese un número: ","número fuera de los límites.")

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

    Parametros: "lista"-> lista de números enteros a recorrer.

    Retorno producto calculado.
    '''
    producto = 1
    for i in lista:
        producto *= i
    
    return producto

#Punto 6. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def buscar_posicion_mayor_valor(lista: list)->int:
    '''
    Busca el número de mayor valor de la lista ingresada y guarda su posición.

    Parametros: "lista" -> lista de números enteros a recorrer.

    Retorno: la posición del elemento de mayor valor.
    '''
    posicion = 0
    numero_mayor = lista[0]
    for i in range(len(lista)):
        if numero_mayor < lista[i]:
            numero_mayor = lista[i]
            posicion = i
    
    return posicion

#Punto 7. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def posiciones_numero_mayor(lista: list)-> None:
    '''
    Muestra por pantalla las posición o posiciones del número más alto en la lista.

    Parametros: "lista" -> lista de números enteros a recorrer.
    '''
    numero_mayor = lista[buscar_posicion_mayor_valor(lista)]

    for i in range(len(lista)):
        if lista[i] == numero_mayor:
            print(f"El número {numero_mayor} se encuentra en el índice {i}")

#Punto 8.

def reemplazar_nombres(lista_nombres:list,
                       nombre_antiguo:str,
                       nombre_nuevo:str)->int:
    '''
    Reemplaza en todas las apariciones de nombre "nombre_antiguo" por "nombre_nuevo" en "lista_nombres".

    Parametros: "lista_nombres" -> lista de nombres a recorrer.
                "nombre_antiguo" -> nombre a reemplazar.
                "nombre_nuevo" -> nombre a agregar a la lista.
    
    Retorno: cantidad de veces que se reemplazó "nombre_antiguo".
    '''
    cantidad_cambios = 0

    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            cantidad_cambios += 1
            lista_nombres[i] = nombre_nuevo
            
    
    return cantidad_cambios

#Punto 9. 

def calcular_interseccion(conjunto_1: list,
                          conjunto_2: list) -> list:
    
    '''
    Cálcula la intersección entre dos conjuntos

    Recibe dos conjuntos de números

    Retorna la intersección en forma de lista
    '''

    #Definimos tamaño de lista de retorno
    if len(conjunto_1) < len(conjunto_2):
        cantidad_retorno = len(conjunto_1)
    else:
        cantidad_retorno = len(conjunto_2)

    #creamos lista de retorno
    interseccion = crear_array(cantidad_retorno)


    #definimos contador para usar como índice
    z = 0

    #buscamos valores repetidos
    for i in range(len(conjunto_1)):

        for j in range(len(conjunto_2)):            

            if conjunto_1[i] == conjunto_2[j]:
                #Agregamos elemento a la intersección en caso de que coincida
                interseccion[z] = conjunto_1[i]
                
                # sumamos 1 al indice de la lista de retorno
                z += 1
                break

    lista_retorno = recortar_lista(interseccion)            
    return lista_retorno

#Punto 10.

def calcular_union(conjunto_1: list,
                    conjunto_2: list)->list:
    
    '''
    Calcula la union entre "conjunto_1" y "conjunto_2".

    Parametros: "conjunto_1" -> conjunto para calcular la unión.
                "conjunto_2" -> conjunto para calcular la unión.
    
    Retorno: Una lista con la unión entre los dos conjuntos.
    '''
    cantidad = len(conjunto_1) + len(conjunto_2)

    lista_retorno = crear_array(cantidad)

    z = 0

    for i in range(len(conjunto_1)):
        lista_retorno[z] = conjunto_1[i]
        z += 1

    for i in range(len(conjunto_2)):

        bandera = False

        for j in range(len(conjunto_1)):

            if conjunto_1[j] == conjunto_2[i]:
                bandera = True
                break
        
        if bandera == False:
            lista_retorno[z] = conjunto_2[i]
            z += 1

    lista_retorno = recortar_lista(lista_retorno)

    return lista_retorno

#Punto 11.

def calcular_diferencia(conjunto_1: list,
                        conjunto_2: list) -> list:
    
    '''
    Calcula la diferencia entre "conjunto_1" y "conjunto_2".

    Parametros: "conjunto_1" -> conjunto que se calcula la diferencia.
                "conjunto_2" -> conjunto que se usa para sacar la diferencia.
    
    Retorno: retorna la diferencia entre los dos conjuntos.
    '''

    diferencia = crear_array(len(conjunto_1))

    z = 0

    for i in range(len(conjunto_1)):

        bandera = True

        for j in range(len(conjunto_2)):

            if conjunto_1[i] == conjunto_2[j]:
                bandera = False
                break
            
        if bandera == True:
            diferencia[z] = conjunto_1[i]
            z += 1

    lista_retorno = recortar_lista(diferencia)

    return lista_retorno


def recortar_lista(lista: list,
                   limite: any = False)->list:

    '''
    Recorta la lista hasta "limite" o hasta llegar al elemento False.

    Parametros: "lista" -> lista a recortar
                "limite" -> indice hasta donde recortar la lista.
    
    Retorno: Retorna una lista recortada.
    '''

    for i in range(len(lista)):
        if lista[i] == limite:
            indice_final = i
            break
    
    lista_retorno = crear_array(indice_final)

    for i in range(len(lista_retorno)):
        lista_retorno[i] = lista[i]

    return lista_retorno
