import random
from .Paquete_Funciones.Input import *


def verificar_ganador_ronda(eleccion_jugador: int, eleccion_maquina: int) -> str:
    '''
    Determina quién ganó la ronda según las elecciones del jugador y la máquina.

    Parametros: "jugador" -> Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera)
                "maquina" -> Elección de la máquina (1 para Piedra, 2 para Papel, 3 para Tijera).
    
    Retorno:    "Jugador" → Si el jugador gana la ronda.
                "Máquina" → Si la máquina gana la ronda.
                "Empate" → Si ambos eligen el mismo elemento.
    '''
    resultado = "Empate"

    if eleccion_jugador == 1 and eleccion_maquina == 3:
        resultado = "Jugador"
    elif eleccion_maquina == 1 and eleccion_jugador == 3:
        resultado = "Máquina"
    elif eleccion_jugador > eleccion_maquina:
        resultado = "Jugador"
    elif eleccion_jugador < eleccion_maquina:
        resultado = "Máquina"
    
    return resultado

def verificar_estado_partida(aciertos_jugador: int,
                            aciertos_maquina: int) -> bool:
    '''
    Determina si la partida sigue en curso o ya ha finalizado.

    Parametros: "aciertos_jugador" -> Cantidad de rondas ganadas por el jugador.
                "aciertos_maquina" -> Cantidad de rondas ganadas por la máquina.
    
    Retorno:    True → Si la partida sigue en curso.
                False → Si la partida ha finalizado (porque alguien ganó dos veces seguidas o se jugaron todas las rondas).  
    '''
    estado_partida = True 

    if aciertos_jugador == 2 or aciertos_maquina == 2:
        return False

    return estado_partida

def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int)->str:
    '''
    Determina quién ganó la partida comparando los aciertos finales.

    Parametros: "aciertos_jugador" -> Cantidad de rondas ganadas por el jugador.
                "aciertos_maquina" -> Cantidad de rondas ganadas por la máquina.
    
    Retorno:    "Jugador" → Si el jugador tiene más aciertos.
                "Máquina" → Si la máquina tiene más aciertos.
    '''
    ganador = "Máquina"
    
    if aciertos_jugador > aciertos_maquina:
        ganador = "Jugador"
    
    return ganador

def mostrar_elemento(eleccion: int)->str:
    '''
    Convierte la elección numérica en un texto legible.

    Parametros: "eleccion" -> Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera).

    Retorno:    "Piedra" cuando su elección == 1.
                "Papel" cuando su elección == 2.
                "Tijera" cuando su  elección == 3.
    '''
    match eleccion:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case _:
            return "Tijera"

def jugar_piedra_papel_tijera() -> None:
    '''
    Jugar al piedra, papel ó tijera.

    Retorna el ganador de la partida ("Jugador" o "Máquina").
    '''
    #Valores iniciales.
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda = 0
    empates = 0

    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda):
        
        #Le pide al usuario que elija un elemento.
        elemento_jugador = get_int(1, 3, "Elija 1 si quiere jugar Piedra, 2 si quiere jugar Papel ó 3 si quiere jugar Tijera: ", "Número inválido. Por favor escriba una de las opciones brindadas.")
        elemento_maquina = random.randint(1,3)

        #Determina el ganador de la ronda.
        ganador_ronda = verificar_ganador_ronda(elemento_jugador, elemento_maquina)

        #Suma la victoria al ganador
        match ganador_ronda:
            case "Jugador":
                aciertos_jugador += 1
            case "Máquina":
                aciertos_maquina += 1
            case _:
                empates += 1
    
        #Suma una ronda
        ronda += 1

        #Muestra por consola la información de la ronda actual
        mostrar_informacion_de_ronda(ronda,elemento_jugador,elemento_maquina,ganador_ronda,aciertos_jugador,aciertos_maquina)
    
    print(f"Ganador de la partida {verificar_ganador_partida(aciertos_jugador, aciertos_maquina)}")

def mostrar_informacion_de_ronda(ronda: int, 
                                elemento_jugador: int,
                                elemento_maquina: int,
                                ganador_ronda:int,
                                aciertos_jugador:int,
                                aciertos_maquina:int)-> None:
    '''
    Muestra por consola la información de la ronda una vez que se haya jugado.

    Parametros: "ronda" -> ronda que se juega.
                "elemento_jugador" -> elemento que eligió el jugador.
                "elemento_maquina" -> elemento que eligió la máquina.
                "ganador_ronda" -> ganador de la ronda actual.
                "aciertos_jugador" -> cantidad de rondas ganadas por el jugador.
                "aciertos_maquina" -> cantidad de rondas ganadas por la máquina.
    '''
    print(f"Ronda {ronda}:\nElemento de Jugador: {mostrar_elemento(elemento_jugador)}\nElemento de Máquina: {mostrar_elemento(elemento_maquina)}")
    match ganador_ronda:
        case "Empate":
            print("La ronda terminó en Empate")
        case _:
            print(f"Ganador de la ronda {ganador_ronda}")   
    print(f"Rondas ganadas por Jugador {aciertos_jugador} y {aciertos_maquina} rondas ganadas por Máquina\n--------------")