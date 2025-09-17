'''
#Punto 1.

def solicitar_entero() -> int: 
    ''
    Solicita un número entero y lo muestra por consola.

    No tiene parametros

    Retorna un número entero.
    ''
    numero = int(input("Ingrese un número entero: "))

    while type(numero) != int:
        print("Tipo de dato incorrecto. Por favor escriba un número entero.")
        numero = int(input("Ingrese un número entero: "))
    
    return numero
    
    
#Punto 2.

def solicitar_flotante() -> float: 
    ''
    Solicita un número flotante y lo muestra por consola.

    No tiene parametros

    Retorna un número flotante.
    ''

    numero = float(input("Ingrese un número flotante: "))
    while type(numero) != float:
        print("Tipo de dato incorrecto. Por favor escriba un número decimal.")
        numero = float(input("Ingrese un número flotante: "))

    return numero

#Punto 3.
def solicitar_cadena() -> str:
    ''
    Solicita una cadena de texto y lo muestra por consola.

    No tiene parametros.

    Retorna un string.
    ''
    texto = str(input("Ingrese un texto: "))
    while type(texto) != str:
        print("Tipo de dato incorrecto. Por favor escriba un texto.")
        texto = str(input("Ingrese un texto: "))
        
    return texto

#Punto 4.
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

def calcular_area_del_rectangulo(base : float,
                                altura : float) -> float:
    ''
    Calcula el area de un rectangulo.

    Tiene dos parametros "base" -> float y "altura" -> float.

    devuelve el "area" -> float. 
    ''
    area = base * altura
    return(area)

print(f"El area del rectángulo es de {calcular_area_del_rectangulo(base, altura)}")

#Punto 5.
from math import pi


radio_circulo = float(input("Ingrese el radio del círculo: "))

def calcular_area_del_ciculo(radio: float) -> float:
    ''
    Calcula el área del circulo.

    Recibe el radio del circulo -> float

    devuelve el "area" del círculo -> float
    ''
    area = pi * (radio**2)
    return(area)


print(calcular_area_del_ciculo(radio_circulo))

#Punto 6.
numero_ingresado = int(input("Ingrese un número: "))

def es_par_o_impar(numero: int) -> None:
    ''
    Indica si el número ingresado es par o impar.

    Recibe un número entero.
    ''
    resto = numero % 2
    if resto == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")

es_par_o_impar(numero_ingresado)

#Punto 7.
numero_ingresado = int(input("Ingrese un número: "))

def definir_par_o_impar(numero: int) -> bool:
    ''
    Indica si el número ingresado es par o impar.

    Recibe un número entero.

    retorna True en caso de que sea par. En caso contrario, retorna falso.
    ''
    resto = numero % 2
    es_par = False

    if resto == 0:
        es_par = True
    
    return es_par
    

print(definir_par_o_impar(numero_ingresado))

#Punto 8.

n1 = float(input("Ingrese un número: "))
n2 = float(input("Ingrese un número: "))
n3 = float(input("Ingrese un número: "))

def guardar_numero_mayor(primer_numero: float, segundo_numero: float, tercer_numero: float) -> float:
    ''
    compara los números pasados y guarda el mayor de ellos.

    Recibe 3 números.

    retorna el número mayor.
    '' 
    numero_mayor = primer_numero
    
    if numero_mayor < segundo_numero:
        numero_mayor = segundo_numero
    if numero_mayor < tercer_numero:
        numero_mayor = tercer_numero
    
    return numero_mayor

print(guardar_numero_mayor(n1,n2,n3))

#Punto 9. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

numero = float(input("Ingrese un número: "))
potencia = float(input("Ingrese la potencia: "))

while potencia < 0:
    potencia = float(input("La potencia debe ser mayor o igual a 0. Por favor escriba otro número: "))

def calcular_potencia(base: float, exponente: float)-> float:
    ''
    Calcula la potencia de "base".

    recibe 2 parametros.

    Retorna el resultado de "base" potenciado por "exponente".
    ''
    numero_potenciado = base ** exponente
    return numero_potenciado

print(calcular_potencia(numero, potencia))

#Punto 10.

numero = int(input("Ingrese un número: "))

def calcular_numero_primo(numero: int)-> bool:
    ''
    Define si el numero ingresado es primo.

    recibe un número entero.

    retorna True en caso de que "numero" sea primo. En caso contrario False.
    ''
    numero_primo = True

    if numero < 2:
        numero_primo = False
    
    limite = (numero // 2) + 1
    for i in range(2 ,limite):
        
        if (numero % i) == 0:
            numero_primo = False
            break
    
    return numero_primo

#Punto 11.

inicio = int(input("Ingrese inicio: "))

fin = int(input("Ingrese fin: "))


def calcular_cantidad_primos(inicio: int, fin: int) -> int:
    ''
    Acumula la cantidad de números primos en el rango dado.

    Recibe dos parametros que definen el rango.

    Retorna la cantidad de numeros primos que hay.
    ''
    cantidad_primos = 0


    for i in range(inicio, fin):

        limite = (i // 2) + 1
        numero_primo = True

        for numero in range(2, limite):
        
            if (i % numero) == 0:
                numero_primo = False
                break

        if numero_primo == True:
            cantidad_primos += 1
    
    return cantidad_primos

print(calcular_cantidad_primos(inicio, fin))

#Punto 12.

numero = float(input("Ingrese el número que desea ver su tabla: "))

def imprimir_tabla_multiplicacion(multiplicando: float) -> None:
    ''
    Calcula la tabla de multiplicación del número ingresado.

    Recibe el número que se quiere calcular su tabla.

    Imprime en consola la tabla del número.
    ''
    #Define la tabla base y le pregunta al usuario si quiere hacer algún cambio.
    rango_de_tabla = range(1, 11)
    bandera = input("Desea poner los limites a la tabla?(S/N): ")
    
    #Chequea que el usuario escriba una opción válida.
    while bandera != "S" and bandera != "N":
        print('Respuesta no reconocida. Por favor escriba en el formato de las opciones "S" ó "N".')
        bandera = input("Desea poner un limite a la tabla?(S/N): ")
    
    #Ejecuta el caso de querer cambiar la tabla.
    if bandera == "S":
        #Solicita los nuevos valores.
        inicio = int(input("Indique el inicio de la tabla: "))
        limite = int(input("Indique el limite de la tabla: "))

        #Corrobora que los valores ingresados tengan sentido.
        while limite <= inicio:
            print("El limite debe ser mayor al inicio de la tabla. A continuación ingrese un nuevo valor de limite o de inicio.")
            inicio = int(input("Indique el inicio de la tabla: "))
            limite = int(input("Indique el limite de la tabla: "))

        #Actualiza la tabla.
        rango_de_tabla = range(inicio, limite + 1)
    
    #Muestra la tabla final.
    for multiplicador in rango_de_tabla:
        producto = multiplicando * multiplicador
        print(f"{multiplicando} x {multiplicador} = {producto}")


'''
def get_int(mensaje: str,
            mensaje_error: str,
            minimo: int,
            maximo: int,
            reintentos: int) -> int|None:
    '''
    Solicita un número al usuario por consola.

    mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
    mínimo: valor mínimo admitido (inclusive).
    máximo: valor máximo admitido (inclusive).
    reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

    Retorna el número entero solicitado. En caso de que el usuario escriba un valor inválido retorna None.
    '''
    print(mensaje)
    numero = int(input("Ingrese un número: "))

    if numero >= minimo and numero <= maximo:
        return numero
    else:
        while reintentos != (-1) and (numero <= minimo or numero >= maximo):
            reintentos -= 1
            numero = int(input("Ingrese un número: "))
        
        if numero >= minimo and numero <= maximo:
            return numero
        else:
            return None
        

def get_string(longitud: int) -> str|None:
    '''
    Valida la longitud de la cadena.

    Recibe un numero entero.

    Retorna la cadena o None.
    '''
    texto = input(f"Ingrese un texto de {longitud} caracteres: ")

    if len(texto) == longitud:
        return texto
    else:
        while len(texto) != longitud:
            print(f"Cantidad de caracteres superior o menor a {longitud}.")
            texto = input(f"Ingrese un texto de {longitud} caracteres: ")
        
        if len(texto) == longitud:
            return texto