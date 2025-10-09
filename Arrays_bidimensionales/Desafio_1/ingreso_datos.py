
from Utilidades import arrays
import funciones_matriz

# desicion = 0
def pedir_desicion():
    '''
    Le pregunta al usuario si quiere ingresar los números de la matriz manualmente.

    Retorno: la desicion del usuario.
    '''
    #Valido la desición.
    desicion = 0

    while desicion != 1 and desicion != 2:
        desicion = int(input("1 si desea ingresar una matriz manualmente y 2 si quiere una aleatoria: "))
    
    return desicion

def crear_matriz_cuadrada()-> list:
    '''
    Crea una matriz cuadrada con el tamaño que desea el usuario.

    Retorno: la matriz creada. 
    '''

    tamanio = int(input("¿De qué tamanio quiere la matriz?: "))
    matriz_creada = funciones_matriz.inicializar_matriz(tamanio,tamanio)

    return matriz_creada

def cargar_eleccion_usuario(desicion: int, 
                            matriz_vacia: list) -> list:
    '''
    Apartir de la elección del usuario. Se cargan los números.

    Parametros: "desicion" -> elección del usuario.
                "matriz" -> matriz a cargar números.
    
    Retorno: La matriz con los números cargados.
    '''
    limite = len(matriz_vacia) ** 2
    if desicion == 1:
        #Carga secuencialmente la matriz de forma manual.
        matriz_cargada = funciones_matriz.carga_secuencial_con_limite(matriz_vacia,f"Ingrese un número entero, que no se repita y que esté en el rango 1 y {limite}: ", limite, f"Error. Número fuera del rango 1 y {limite}.")
    
    else:
        #Carga secuencialmente la matriz de forma automática.
        matriz_cargada = funciones_matriz.cargar_secuencial_random(matriz_vacia, limite)

    return matriz_cargada


def validar_numeros_repetidos(matriz: list)-> bool:
    '''
    Valida si hay algún número repetido en "matriz"

    Retorno: True -> si hay un número repetido.
             False -> en caso de que no se repita algún número.
    '''
    #Creamos el array con los valores de la matriz.
    array_numeros = crear_array_de_matriz(matriz)
    
    #Validamos si hay número repetido.
    for i in range(len(array_numeros)):
        for j in range(i + 1 ,len(array_numeros)):
            if array_numeros[i] == array_numeros[j]:
                return True
    
    return False


def crear_array_de_matriz(matriz: list)-> list:
    '''
    Crea un array con todos los elementos de "matriz".

    Parametros: "matriz" -> matriz a copiar los elementos.

    Retorno: array con los elementos de "matriz".
    '''
    array_numeros = arrays.crear_array(len(matriz) * len(matriz[0]))

    indice = 0

    #Cargamos los valores de la matriz al array.
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            array_numeros[indice] = matriz[i][j]
            indice += 1


