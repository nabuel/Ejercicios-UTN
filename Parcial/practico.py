import funciones
planilla = [[1,2,3,4],
            [0,23,2,1],
            [1,2,3,6]]

salones = ["Puerto Madero", "Palermo", "San Telmo"]
eventos = ["cumpleaños", "casamientos", "fiestas de 15", "bodas de oro"]
valor_eventos =  [100000, 2000000, 100000, 200000]


bandera = True

while bandera:
    desicion = 0

    print("---------------------")
    print("1- Cargar planilla de recaudacion")
    print("2- Mostrar la cantidad de eventos por cada tipo de evento")
    print("3- Mostrar el nombre del evento mas realizado en cada salon")
    print("4- Mostrar la recaudacion por salon")
    print("5- Mostrar los salones que generaron mas de 5 millones en casamientos")
    print("6- Mostrar el porcentaje de bodas de oro por salon")
    print("7- Mostrar la recaudacion de cada salon ordenada de mayor a menor")
    print("8- Salir del menu")
    print("---------------------")

    desicion = funciones.get_int("Elija una de las opciones: ", "Opción no válida.")
    print()

    match desicion:
        case 1:    
            for i in range(len(planilla)):
                for j in range(len(planilla[i])):
                    planilla[i][j]= planilla[i][j] + funciones.get_int(f"La cantidad de {eventos[j]} realizados en {salones[i]}: ", "Por favor, ingrese un número.")
        case 2:
            funciones.calcular_cantidad_fiestas(planilla, salones)
        case 3:
            funciones.buscar_evento_mas_realizado(planilla, salones, eventos)
        case 4:
            funciones.calcular_recaudacion_por_salon(planilla, salones, valor_eventos)
        case 5:    
            contador = 0
            for i in range(len(planilla)):
                if planilla[i][1] * valor_eventos[1] > 5000000:
                    contador += 1
            print(f"{contador} salones generaron más de 5000000$ con los casamientos.")
        case 6:
            porcentaje_mayor = 0
            salon_porcentaje_mayor = salones[0]

            for i in range(len(planilla)):
                porcentaje = funciones.calcular_porcentaje_bodas_del_salon(planilla[i])
                print(f"El porcentaje de la bodas de oro del salón de {salones[i]} es de {porcentaje}%")
                print()

                if porcentaje > porcentaje_mayor:
                    porcentaje_mayor = porcentaje
                    salon_porcentaje_mayor = salones[i]

            print(f"El salón con mayor porcentaje de bodas de oro realizadas es el de {salon_porcentaje_mayor} con {porcentaje_mayor}%")
        case 7:
            recaudacion = [False] * len(salones)

            for i in range(len(recaudacion)):
                recaudacion[i] = funciones.calcular_recaudacion_del_salon(planilla[i], valor_eventos)

            recaudacion = funciones.ordenar_lista_mayor_menor(recaudacion)
            print(f"La recaudación de los salones es de: ")
            for i in range(len(recaudacion)):
                print(f"{i + 1}- {recaudacion[i]}$ ", end="")
                print()
                
        case _:
            print("Adiós.")
            bandera = False


