# Simulador sistema doblarse B/R en la ruleta
from random import randint

BANCA = {"1": 5, "2": 10, "3": 20, "4": 50, "5": 100, "6": 200, "7": 500}
BLACK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


def definir_Dinero():
    dinero = 0
    try:
        dinero = int(input(
            "Introduzca el dinero total en fichas para la simulación, por defecto 1000€: "))
    except ValueError:
        dinero = 1000
    finally:
        return dinero


def apostar(fichas_base, fichas_totales, predicion, n_simulaciones, dinero):
    ganadas = 0
    perdidas = 0
    total = fichas_totales
    fichas = 1
    if predicion == RED:
        color = "RED"
    else:
        color = "BLACK"
    for tir in range(1, n_simulaciones+1):
        if total == 0:
            break
        if predicion == RED:
            color = "RED"
            c_color = "BLACK"
        elif predicion == BLACK:
            color = "BLACK"
            c_color = "RED"
        total -= fichas  # Haces la apuesta
        tirada = randint(0, 36)  # Hace la tirada
        if tirada in predicion:  # Si acierta
            ganancias = fichas * 2
            total += ganancias
            ganadas += 1
            if n_simulaciones == tir:
                print(
                    f"Tirada nº{tir} Has acertado {tirada} {color}\nRecojes de la mesa {ganancias} fichas, tienes {total} fichas en Mano\nResultado: EXITO\n")
                break
            print(
                f"Tirada nº{tir} Has acertado {tirada} {color}\nRecojes de la mesa {ganancias} fichas, cambias a {c_color} y apuestas 1 ficha, ahora tienes {total - 1} fichas en Mano\n")
            if predicion == BLACK:
                predicion = RED
                color = "RED"
            else:
                predicion = BLACK
                color = "BLACK"
            fichas = 1
        else:  # Si Falla
            if tirada == 0:  # Si es 0 cambia el color a GREEN
                c_color = "GREEN"
            perdidas += 1
            if total == 0:  # Si no quedan fichas
                print(
                    f"Tirada nº{tir} {tirada} {c_color} Has PERDIDO\nTienes {total} fichas en Mano\nResultado: FRACASO\n")
                break
            if n_simulaciones == tir:  # Si es la Ultima tirada y es un Fracaso
                print(
                    f"Tirada nº{tir} {tirada} {c_color} Has PERDIDO\nTienes {total} fichas en Mano\nResultado: NEUTRO\n")
            elif total - fichas <= 0:  # Si NO se puede seguir doblando
                if total >= 1:
                    fichas = 1
                    print(
                        f"Tirada nº{tir} {tirada} {c_color} Has PERDIDO\nVuelves a apostar al {color} otras {fichas} fichas, ahora tienes {total-fichas} fichas en Mano\n")
            elif total - fichas * 2 >= 0:  # Si SI se puede seguir doblando
                fichas *= 2
                print(
                    f"Tirada nº{tir} {tirada} {c_color} Has PERDIDO\nVuelves a apostar al {color} otras {fichas} fichas, ahora tienes {total-fichas} fichas en Mano\n")
    # Final de las tiradas totales
    print(
        f"Has tirado {tir} veces de {n_simulaciones} y tienes un total de {total} fichas de {fichas_totales} fichas iniciales, {total*100//fichas_totales}% del inicio")
    print(
        f"Tienes {total * fichas_base}€ en total de {fichas_totales * fichas_base}€ iniciales\n")
    print(f"{ganadas * 100 // (ganadas+perdidas)}% de aciertos\n")
    print(
        f"GANADAS: {ganadas}\nPERDIDAS: {perdidas}\n")


def main():
    print("-Simulador de Doble o Nada en la ruleta-")
    dinero = definir_Dinero()
    n_simulaciones = int(input("Cuantas tiradas quieres simular?: "))
    fichas = input(f"Tienes {dinero}€, cual quieres que sea la apuesta base?: \n" +
                   "1- 5€ | 2- 10€ | 3- 20€ | 4- 50€ | 5- 100€ | 6- 200€ | 7- 500€: ")
    fichas_base = BANCA[fichas]  # Valor de las fichas
    fichas_totales = dinero // fichas_base  # Total de fichas para jugar
    color = input(f"Elije color inicial (B - R)")  # Elige el color de inicio
    if color == "r":
        color = RED
    else:
        color = BLACK
    apostar(fichas_base, fichas_totales, color, n_simulaciones, dinero)
    input("Pulse Enter para Salir")


if __name__ == "__main__":
    main()
