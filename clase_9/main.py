from Utilidades.Array_Generales import *
from Utilidades.Especificas import *
from Utilidades.Input import *

def arrays_numeros():
    '''
    Hace funcionar el desafio de "arrays numeros".
    '''
    #Muestra las opciones del menú.
    mostrar_menu()

    #Le pide al usuario que elija una de las opciones.
    decision = get_int(1,7,"Elija una de las opciones.", "Número fuera de las opciones.", 1000000000000)

    #Le pide al usuario que ingrese 10 números si elije una función que necesite una lista.
    if decision != 7:
        print("A continuación escribirá 10 números enteros. Los valores permitidos son desde -1000 a 1000.")
        lista = ingresar_datos()
        print("---------------------")

    while decision != 7:
        match decision:
            case 1:
                contar_positivos_negativos(lista)
            case 2:
                sumar_numeros_pares(lista)
            case 3:
                calcular_mayor_impar(lista)
            case 4:
                listar_numeros(lista)
            case 5:
                listar_pares(lista)
            case 6:
                listar_numeros_posicion_impar(lista)
    
        #Pregunta si el usuario quiere ver el menú.
        ver_menu = get_int(1,2,"¿Desea ver el menú nuevamente?(1-SI,2-NO)", "Error,número inválido.", 100000000000)
        if ver_menu == 1:
            mostrar_menu()

        decision = get_int(1,7,"Elija una de las opciones.", "Número fuera de las opciones.", 1000000000000)
