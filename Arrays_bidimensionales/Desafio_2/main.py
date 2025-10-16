import validacion_lineas_coches
import calculos_recaudaciones, generacion_verificacion_existencia_legajo, ingreso_datos, utilidades


#Filas = lineas de colectivo. Columnas = cantidad de colectivos por línea.
registro_colectivos = [[1,2,3,4,5],
                      [1,2,3,4,5],
                      [1,2,3,4,5]]

legajos = generacion_verificacion_existencia_legajo.crear_legajos(15)

#Crea la planilla.
planilla = utilidades.inicializar_matriz(len(registro_colectivos),len(registro_colectivos[0]),0)

bandera = True
while bandera:

    print("1- si quiere cargar la planilla de recaudación.")
    print("2- si quiere mostrar la recaudación de cada coche y linea.")
    print("3- si quiere calcular y mostrar la recaudación por línea.")
    print("4- si quiere calcular y mostrar la recaudación por coche.")
    print("5- si quiere calcular y mostrar la recaudación total.")
    print("6- si quiere salir del programa.")
    print("---------------------------------")

    eleccion = ingreso_datos.get_int("Elija una de las opciones: ", "Por favor escriba un número.")
    print("")

    match eleccion:
        case 1: 
            print(legajos)
            planilla = calculos_recaudaciones.cargar_planilla_recaudacion(legajos,registro_colectivos, planilla)
            print("")
        case 2:
            utilidades.mostrar_matriz(planilla, "$")
            print("")
        case 3:
            calculos_recaudaciones.calcular_suma_mostrar_linea(planilla,"Lo recaudado por la línea ", " $")
            print("")
        case 4:
            colectivo = ingreso_datos.get_int("Ingrese el número del coche: ", "Debe ingresar un número.")
            if validacion_lineas_coches.validar_coche(colectivo, registro_colectivos):
                calculos_recaudaciones.calcular_suma_mostrar_columna(planilla, "Lo recaudado por el colectivo ", " $", colectivo)
            else:
                print("Colectivo innexistente.")
            print("")
        case 5:
            calculos_recaudaciones.calcular_suma_mostrar(planilla, "Lo recaudado por los colectivos es : ", " $")
            print("")
        case 6:
            print("Adiós.")
            bandera = False
        case _:
            print("Número fuera de los límites. Por favor elija una de las opciones.")
            print("")





