# Realiza un juego de piedra, papel o tijeras. En este caso, jugaremos al mejor de tres.
import random


def eleccion():
    elec = int(input("Ingrese su elección: "))
    if elec == 1:
        print("su eleccion es piedra")
    elif elec == 2:
        print("su eleccion es papel")
    elif elec == 3:
        print("su eleccion es tijera")
    else:
        print("Le erraste de número")
        return False
    return elec


def maquina():
    elecmaquina = random.randint(1, 3)
    if elecmaquina == 1:
        print("La elección del robot es piedra")
    elif elecmaquina == 2:
        print("La eleccion del robot es papel")
    elif elecmaquina == 3:
        print("La elección del robot es tijera")
    return elecmaquina


def ganador(x, y):
    print("------------------------------------------------")
    if x == y:
        print("Empate")
        print("---------------------------------------------------")
        return 0
    elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
        print("¡Gana el robot!")
        print("---------------------------------------------------")
        return -1
    elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
        print("¡Ganaste!")
        print("---------------------------------------------------")
        return 1


def jugar():
    contador = 0
    for i in range(3):
        print("Inserte elección: ", "\n 1-Piedra", "\n 2-Papel", "\n 3-Tijera")
        x = eleccion()
        y = maquina()
        contador += (ganador(x, y))
    print("*****************************************************")
    if contador == 0:
        print("Partida empatada")
    elif contador > 0:
        print("¡Partida ganada, felicitaciones! ※\(^o^)/※")
    elif contador < 0:
        print("Partida perdida. Game Over 	╚(•⌂•)╝")
    print("*****************************************************")


# main
jugar()
