# Realiza un juego de piedra, papel o tijeras.
import random


def eleccion():
    eleccion = int(input("Ingrese su elección: "))
    mano = ()
    mano = eleccion
    if mano == 1:
        print("su eleccion es piedra")
    elif mano == 2:
        print("su eleccion es papel")
    elif mano == 3:
        print("su eleccion es tijera")
    else:
        print("Le erraste de número")
        return False
    return mano


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
    print("***********************************************")
    if x == y:
        print("Resultado: Empate")
    elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
        print("Fuiste derrotado por el robot. Game Over")
    elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y ==2):
        print("¡Ganaste!")
    print("***********************************************")


# Main
print("Inserte su elección: ", "\n 1-Piedra", "\n 2-Papel", "\n 3-Tijera")
x = eleccion()
y = maquina()
ganador(x, y)