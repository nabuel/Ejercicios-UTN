'''
#Punto 1.

def solicitar_entero() -> None: 
    ''
    Solicita un número entero y lo muestra por consola.

    No tiene parametros

    Retorna un número entero.
    ''
    numero = int(input("Ingrese un número entero: "))
    print(numero)
    
    
#Punto 2.

def solicitar_flotante() -> float: 
    ''
    Solicita un número flotante y lo muestra por consola.

    No tiene parametros

    Retorna un número flotante.
    ''

    numero = float(input("Ingrese un número flotante: "))
    return(numero)

#Punto 3.
def solicitar_cadena() -> str:
    ''
    Solicita una cadena de texto y lo muestra por consola.

    No tiene parametros.

    Retorna un string.
    ''
    texto = str(input("Ingrese un texto: "))
    return(texto)

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


'''
