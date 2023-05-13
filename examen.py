"""1. Escriba un programa que muestre una partida de dados
entre dos jugadores, se debe ingresar la cantidad de turnos
que se van a jugar, cada jugador tira un dado. Si un jugador
saca un valor mayor que el otro, gana los puntos de ambos
dados. Si los dos jugadores sacan el mismo valor, ninguno
recibe puntos. Si al finalizar la partida hay un empate,
ninguno gana la partida. Debe mostrar quien gana la partida,
quien gana cada turno y la puntuación acumulada por cada
jugador.
Para el examen pueden usar la librería random (import
random) y utilizar el método random.randint(desde, hasta)
que toma números enteros de forma aleatorias según rango
dado."""

import random

def partida(turnos):
    puntosPrimerJugador = 0
    puntosSegundoJugador = 0

    for turno in range(1, turnos + 1):
        print(f"Turno {turno}:")
        dadoPrimerJugador = random.randint(1, 6)
        dadoSegundoJugador = random.randint(1, 6)
        print(f"Jugador 1: {dadoPrimerJugador}")
        print(f"Jugador 2: {dadoSegundoJugador}")

        if dadoPrimerJugador > dadoSegundoJugador:
            puntosPrimerJugador += dadoPrimerJugador + dadoSegundoJugador
            print("Jugador 1 gana el turno.")
        elif dadoPrimerJugador < dadoSegundoJugador:
            puntosSegundoJugador += dadoPrimerJugador + dadoSegundoJugador
            print("Jugador 2 gana el turno.")
        else:
            print("Empate. Ningún jugador recibe puntos.")

        print(f"Puntuación acumulada:")
        print(f"Jugador 1: {puntosPrimerJugador}")
        print(f"Jugador 2: {puntosSegundoJugador}")
        print("--------------------")

    if puntosPrimerJugador > puntosSegundoJugador:
        print("Jugador 1 gana la partida.")
    elif puntosPrimerJugador < puntosSegundoJugador:
        print("Jugador 2 gana la partida.")
    else:
        print("Empate. Ningún jugador gana la partida.")

turnos = int(input("Cuantos turnos desea jugar: "))
partida(turnos)
