
from ingreso_datos import *
from generacion_verificacion_existencia_legajo import *
import validacion_lineas_coches


def actualizar_recaudacion(linea, coche, planilla)-> list:
    '''
    actualiza el monto de recaudación del colectivo.
    '''
    monto = get_int("Ingrese el monto de recaudación: ", "Ingrese un número entero.")

    planilla[linea - 1][coche - 1] += monto

    return planilla

def cargar_planilla_recaudacion(lista_legajos: list, 
                                registro_colectivos: list,
                                planilla: list) -> list|None:
    '''
    Carga la planilla de recaudación.

    Retorno: la planilla de recaudación cargada.
    '''
    #Solicita el número de legajo del chofer.
    chofer = get_int("Ingrese su número de legajo: ", "Debe ingresar un número.")
    
    #Válida la existencia del chofer.
    if validar_numero(lista_legajos, chofer):
        bandera = True
        #Datos para cargar la recaudación del bondi.
        while bandera:
            linea = get_int("Ingrese el número de la línea: ", "Debe ingresar un número.")
            coche = get_int("Ingrese el número del coche: ", "Debe ingresar un número.")
            #Válido que exista el colectivo.
            if validacion_lineas_coches.validar_colectivo(linea, coche, registro_colectivos):
                #Actualizo la recaudación.
                planilla_cargada = actualizar_recaudacion(linea, coche, planilla)
            else:
                print("Colectivo inexistente.")
            seguir_cargando = get_int("Ingrese 1 si no quiere seguir cargando: ", "Ingrese un número.")
            if seguir_cargando == 1:
                bandera = False
        
        return planilla_cargada
    else:
        print("Número de legajo no encontrado.")
        return planilla


def calcular_suma_mostrar_linea(matriz: list,
                                mensaje = "El resultado de la fila ",
                                mensaje_final = ".")-> None:
    '''
    Calcula la suma de los elementos y muestra por pantalla el resultado de cada linea.
    '''
    for i in range(len(matriz)):
        resultado = 0
        for j in range(len(matriz[i])):
            resultado += matriz[i][j]
        print(mensaje + f"{i + 1} es : {resultado}" + mensaje_final)

def calcular_suma_mostrar_columna(matriz: list, 
                                  mensaje = "El resultado de la columna ",
                                  mensaje_final = ".",
                                  columna = 0):
    '''
    Calcula la suma de los elementos y muestra por pantalla el resultado de la columna indicada.
    '''
    resultado = 0
    for i in range(len(matriz)):
        resultado += matriz[i][columna - 1]

    print(mensaje + f"{columna} es : {resultado}" + mensaje_final)

def calcular_suma_mostrar(matriz: list,
                          mensaje = "La suma total es ",
                          mensaje_final = ".")-> None:
    '''
    Calcula la suma de todos los elementos de la matriz y lo muestra por pantalla. 
    '''
    resultado = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado += matriz[i][j]
    
    print(mensaje + f"{resultado}" + mensaje_final)