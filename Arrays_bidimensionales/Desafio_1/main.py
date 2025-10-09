
from ingreso_datos import *
from validacion_magico import validar_matriz_magica
import funciones_matriz


desicion = pedir_desicion()


matriz_vacia = crear_matriz_cuadrada()


matriz_cargada = cargar_eleccion_usuario(desicion,matriz_vacia) 



funciones_matriz.mostrar_matriz(matriz_cargada)

if validar_matriz_magica(matriz_cargada):
    print("Es matriz mágica.")
else:
    print("No es matriz mágica.")























def mostrar_matriz_magica():
    '''
    Muestra los resultados de la matriz. 
    '''


