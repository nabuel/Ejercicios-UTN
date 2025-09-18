import random
from .Paquete_Funciones.Input import *


def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    '''
    Determina quién ganó la ronda según las elecciones del jugador y la máquina.

    Parametros: "jugador" -> Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera
                "maquina" -> Elección de la máquina (1 para Piedra, 2 para Papel, 3 para Tijera).
    
    Retorno:    "Jugador" → Si el jugador gana la ronda.
                "Máquina" → Si la máquina gana la ronda.
                "Empate" → Si ambos eligen el mismo elemento.
    '''
    if jugador == 1 and maquina == 3:
        return "Jugador"
    elif jugador == 3 and maquina == 1:
        return "Máquina"
    elif jugador > maquina:
        return "Jugador"
    elif jugador < maquina:
        return "Máquina"
    else:
        return "Empate"

def verificar_estado_partida(aciertos_jugador: int,
                            aciertos_maquina: int,
                            ronda_actual: int) -> bool:
    '''
    Determina si la partida sigue en curso o ya ha finalizado.

    Parametros: "aciertos_jugador" -> Cantidad de rondas ganadas por el jugador.
                "aciertos_maquina" -> Cantidad de rondas ganadas por la máquina.
                "ronda_actual"     -> Número de la ronda actual.
    
    Retorno:    True → Si la partida sigue en curso.
                False → Si la partida ha finalizado (porque alguien ganó dos veces seguidas o se jugaron todas las rondas).  
    '''
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        return False
    elif ronda_actual >= 3:
        if aciertos_jugador == 2 or aciertos_maquina == 2:
            return False
        return True
    else:
        return True

def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int)->str:
    '''
    Determina quién ganó la partida comparando los aciertos finales.

    Parametros: "aciertos_jugador" -> Cantidad de rondas ganadas por el jugador.
                "aciertos_maquina" -> Cantidad de rondas ganadas por la máquina.
    
    Retorno:    "Jugador" → Si el jugador tiene más aciertos.
                "Máquina" → Si la máquina tiene más aciertos.
    '''
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        return "Máquina"
    

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

def jugar_piedra_papel_tijera() -> str:
    '''
    Jugar al piedra, papel ó tijera.

    Retorna el ganador de la partida ("Jugador" o "Máquina").
    '''
    #Valores iniciales.
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda = 0
    empates = 0
    #Le pide al usuario que elija un elemento.
    elemento_jugador = get_int(1, 3, "Elija 1 si quiere jugar Piedra, 2 si quiere jugar Papel ó 3 si quiere jugar Tijera: ", "Número inválido. Por favor escriba una de las opciones brindadas.")
    elemento_maquina = random.randint(1,3)

    #Determina el ganador de la ronda.
    ganador_ronda = verificar_ganador_ronda(elemento_jugador, elemento_maquina)
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
    print(f"Ronda {ronda}:\nElemento de Jugador: {mostrar_elemento(elemento_jugador)}\nElemento de Máquina: {mostrar_elemento(elemento_maquina)}")
    match ganador_ronda:
        case "Empate":
            print("La ronda terminó en Empate")
        case _:
            print(f"Ganador de la ronda {ganador_ronda}")   
    print(f"{aciertos_jugador} rondas ganadas por Jugador y {aciertos_maquina} rondas ganadas por Máquina\n--------------")

    #Sigue jugando la partida.
    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda):
        #Le pide al usuario que elija un elemento.
        elemento_jugador = get_int(1, 3, "Elija 1 si quiere jugar Piedra, 2 si quiere jugar Papel ó 3 si quiere jugar Tijera: ", "Número inválido. Por favor escriba una de las opciones brindadas.")
        elemento_maquina = random.randint(1,3)

        #Determina el ganador de la ronda.
        ganador_ronda = verificar_ganador_ronda(elemento_jugador, elemento_maquina)
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
        print(f"Ronda {ronda}:\nElemento de Jugador: {mostrar_elemento(elemento_jugador)}\nElemento de Máquina: {mostrar_elemento(elemento_maquina)}")
        match ganador_ronda:
            case "Empate":
                print("La ronda terminó en Empate")
            case _:
                print(f"Ganador de la ronda {ganador_ronda}")   
        print(f"Rondas ganadas por Jugador {aciertos_jugador} y {aciertos_maquina} rondas ganadas por Máquina\n--------------")
    
    print(f"Ganador de la partida {verificar_ganador_partida(aciertos_jugador, aciertos_maquina)}")


    