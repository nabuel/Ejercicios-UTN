import Funciones

Tema = "Bradley Cooper | Lukas Nelson - Shallow"
Vistas = "1900 millones"
Duración = "3:37"
Link = "https://www.youtube.com/watch?v=bo_efYhYU2A"
Fecha_de_lanzamiento = "2018-09-27"

#Punto 1.
def obtener_colaboradores(titulo: str) -> list:
    '''
    Obtiene el nombre de los colaboradores de la canción.

    Retorno: una lista con los colaboradores (excluyendo el nombre del tema).
    '''
    lista_colaboradores = [False] * len(titulo)

    for i in range(len(titulo)):
        if ord(titulo[i]) == 45:
            break
        lista_colaboradores[i] = titulo[i]
    
    lista_colaboradores = Funciones.recortar_lista(lista_colaboradores)

    return lista_colaboradores



#Punto 2.
def obtener_nombre_tema(titulo: str) -> str:
    '''
    Obtiene el nombre del tema.

    Retorno: el nombre del tema sin los colaboradores.
    '''
    

    indice_corte = len(titulo)
    for i in range(len(titulo)):
        if ord(titulo[i]) == 45:
            indice_corte = i + 1
            break

    nombre = [False] * (len(titulo) - indice_corte)
    indice = 0
    for j in range(indice_corte, len(titulo)):
        nombre[indice] = titulo[j]
        indice += 1
    
    return nombre


#Punto 3.

def convertir_vistas_numerico(vistas: str) -> int:
    '''
    Convierte la cantidad de vistas a un número entero en millones.

    Retorno: la cantidad de vistas.
    '''
    numero_retorno = 0
    
    #Buscar número.
    indice_corte = len(vistas)
    for i in range(len(vistas)):
        if not Funciones.validar_numero(vistas[i]):
            break
        indice_corte = i
    
    digitos = indice_corte

    for j in range(len(vistas)):
        if indice_corte == j:
            break

        numero = int(vistas[j])

        for _ in range(digitos):
            numero = numero * 10
        
        numero_retorno += numero
        digitos -= 1

    numero_retorno += int(vistas[j])
    numero_retorno = numero_retorno * 1000000

    return numero_retorno


def convertir_vistas_numerico_luca(vistas: str)-> int:

    numero = 0
    largo = 0

    for i in range(len(vistas)):
        if Funciones.validar_numero(vistas[i]):
            largo += 1
    indice = largo

    match indice:
        case 4:
            indice = 1000
        case 5:
            indice = 10000
        case 6:
            indice = 100000
        case 7:
            indice = 1000000


    for i in range(len(vistas)):
        if vistas[i] == "0":
            indice = indice // 10
            continue

        if not Funciones.validar_numero(vistas[i]):
            break

        numero += int(vistas[i]) * indice
        indice = indice // 10

    
    numero * 1000000

    return numero


#Punto 4.
def convertir_duracion_numerico(duracion: str) -> int:
    '''
    Convierte la duración del video a segundos.

    Retorno: la duración en segundos.
    '''    
    #Calcula los minutos a segundos.
    minutos = calcular_minutos(duracion)
    #Calcular segundos.
    
    segundos = calcular_segundos(duracion)
    

    segundos += minutos * 60

    return segundos


def calcular_minutos(duracion: list)-> int:
    '''
    Calcula los minutos del video.

    Retorno: la cantidad de minutos del video.
    '''
    indice_minutos = 0
    for i in range(len(duracion)):
        if ord(duracion[i]) == 58:
            break
        indice_minutos = i
    minutos = [False] * (indice_minutos + 1)

    for j in range(len(minutos)):
        minutos[j] = duracion[j]
    
    total_minutos = 0
    if len(minutos) == 1:
        total_minutos = int(minutos[0])
    else:
        total_minutos = int(minutos[0]) * 10
        total_minutos += int(minutos[1])
    
    return total_minutos

def calcular_segundos(duracion: list)-> int:
    '''
    Calcula los segundos del video.

    Retorno: los segundos.
    '''
    for i in range(len(duracion)):
        if ord(duracion[i]) == 58:
            indice_segundos = i + 1
    
    segundos = [False] * (indice_segundos)

    for n in range(len(segundos)):
        if n == 0:
            segundos[n] = duracion[indice_segundos]
        else:
            segundos[n] = duracion[indice_segundos + 1]
    
    for j in range(len(segundos)):
        if j == 0:
            total_segundos = int(segundos[j]) * 10
        else:
            total_segundos += int(segundos[j])
    
    return total_segundos


def obtener_codigo(url: str) -> str:
    '''
    Extrae el código único del video.

    Retorno: El código único del video.
    '''
    #Busca el indice del =.
    for i in range(len(url)):
        indice_corte = i
        if ord(url[i]) == 61:
            break

    codigo_retorno = [False] * len(url)
    indice = 0
    for j in range(len(url)):
        if j > indice_corte:
            codigo_retorno[indice] = url[j]
            indice += 1
    
    codigo_retorno = Funciones.recortar_lista(codigo_retorno)

    return codigo_retorno

Funciones.mostrar_array(obtener_codigo(Link))

