
#Punto 1.
def sumar_naturales(numero: int)->int:
    if numero == 1:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)

# print(sumar_naturales(5))

#Punto 2.
def calcular_potencia(base: int, exponente: int)->int:
    if exponente == 0:
        return 1 
    else: 
        resultado = calcular_potencia(base, exponente - 1) * base
    return resultado

# print(calcular_potencia(4,3))

#Punto 3.
def sumar_digitos(numero: int) ->int:
    if numero < 10:
        return numero
    else:
        return sumar_digitos(numero // 10) +  numero % 10

print(sumar_digitos(123))

#Punto 4.Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

def calcular_fibonacci(numero: int)->int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

# print(calcular_fibonacci(10))