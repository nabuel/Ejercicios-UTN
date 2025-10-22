import Ingreso_datos, Funciones, Verificaciones

ejecutar = True

matriz = [[0,2,4],
          [6,8,10],
          [12,14,16]]

while ejecutar:
    print("1- Ingreso de matriz.")
    print("2- Verificar la existencia de secuencias de números consecutivos pares.")
    print("3- Determinar la cantidad de ocurrencias.")
    print("4- Identificar la secuencia más corta.")
    print("5- Identificar la secuencia más larga.")
    print("6- Salir del programa.")
    print("-----------------------")

    decision = Ingreso_datos.get_int("Elija una de las opciones: ")

    match decision:
        case 1:
            fila = Ingreso_datos.get_int("Indique la cantidad de filas: ")
            columna = Ingreso_datos.get_int("Indique la cantidad de columnas: ")
            carga_manual = Ingreso_datos.get_int("1 si quiere cargar los números manualmente: ")
            matriz = Funciones.crear_matriz(fila, columna)
            if carga_manual == 1:
                matriz = Funciones.cargar_matriz_secuencial(matriz)
            else:
                limite = Ingreso_datos.get_int("Indique un límite de números permitidos: ")
                matriz = Funciones.cargar_matriz_random(matriz, limite)
            print("")
        case 2:
            Verificaciones.verificar_secuencias_pares_matriz(matriz)
        case 3:
            cantidad = Funciones.contar_secuencias_pares_matriz(matriz)
            print(f"Hay {cantidad} secuencias de números pares.")
        case 4:
            secuencia = buscar_secuencia_corta_pares(matriz)
            print("La secuencia más corta de pares consecutivos es:")
            mostrar_array(secuencia)
        case 5:
            secuencia = buscar_secuencia_larga_pares(matriz)
            print("La secuencia más larga de pares consecutivos es:")
            mostrar_array(secuencia)
        case 6:
            print("Adiós.")
            ejecutar = False
        case _:
            print("Por favor elija una de las opciones.")
            