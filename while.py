encuestado = 0

#El empleado tipo "a" es el empleado de género masculino que vota por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
empleados_tipo_a = 0

#El empleado tipo "b" es el empleado que no votaron por IA, no sea de género Femenino y su edad esté entre los 33 y 40 años.
empleados_tipo_b = 0

#Edad de comparación inicial ya que el usuario si o si es mayor de edad.
edad_empleado_mayor_actual = 0

#Recolección de datos.

while encuestado < 10:
    #Pide los datos al usuario
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su género (Masculino, Femenino, Otro): ")
    tecnologia_elegida = input("Elija una tecnología (IA, RV/RA, IOT): ")

    #En caso de que el usuario escriba una edad inválida se le solicita que la vuelva a escribir.
    while edad < 18 or edad > 60:
        if edad < 18:
            print(f"Ingrese una edad mayor a {edad}")
            edad = int(input("Ingrese su edad: "))
        elif edad > 60:
            print(f"Ingrese una edad menor a {edad}")
            edad = int(input("Ingrese su edad: "))
        
    #En caso de que el usuario escriba un género distinto a las opciones, se le solicita que escriba un de las opciones.
    while genero != "Masculino" or genero != "Femenino" or genero != "Otro":
        print("Genero desconocido. Por favor elija una de las opciones.")
        genero = input("Ingrese su género (Masculino, Femenino, Otro): ")


    #En caso de que la tecnologia elegida no sea una de las opciones dadas, se le pide que elija una nuevamente.
    while tecnologia_elegida != "IA" and tecnologia_elegida != "RV/RA" and tecnologia_elegida != "IOT":
        print("Tecnologia desconocida. Por favor elija una de las opciones.")
        tecnologia_elegida = input("Elija una tecnología (IA, RV/RA, IOT): ")

    #Filtro por tecnologia.
    match tecnologia_elegida:
        case "IA":
            if genero == "Masculino" and (edad >= 25 and edad <= 50):
                empleados_tipo_a += 1
        case "IOT":
            if genero == "Masculino" and (edad >= 25 and edad <= 50):
                empleados_tipo_a += 1
                if edad >= 33 and edad <= 40:
                    empleados_tipo_b += 1
            elif genero == "Otro" and (edad >= 33 and edad <= 40):
                empleados_tipo_b += 1
        case "RV/RA":
            if genero != "Femenino" and (edad >= 33 and edad <= 40):
                empleados_tipo_b += 1
    
    #Recuerda el empleado de mayor edad másculino.
    if (edad_empleado_mayor_actual < edad) and genero == "Masculino":
        nombre_empleado_mayor = nombre
        tecnologia_elegida_empleado_mayor = tecnologia_elegida
        edad_empleado_mayor_actual = edad
    
    #Suma una vuelta al contador
    encuestado += 1

porcentaje_empleados_tipo_b = (empleados_tipo_b * 100) / encuestado
print(f'cantidad de empleados tipo "a" {empleados_tipo_a}.\nPorcentaje de empleados tipo "b" {porcentaje_empleados_tipo_b}.')
if edad_empleado_mayor_actual != 0:
    print(f"Nombre del empleado de mayor edad: {nombre_empleado_mayor}, la tecnologia que votó {tecnologia_elegida_empleado_mayor}.")