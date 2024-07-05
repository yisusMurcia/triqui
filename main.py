"""Triqui
Autor: Jesús Antonio Murcia
05-07-2024"""

def leerOpcion():
    opcion = input("Seleccion una opción: ")
    while len(opcion) != 1 or opcion not in "012":
        print("Selecciona una opción válida, vuelve a intentarlo")
        opcion = input("Introduce tu opción: ")
    return int(opcion)

def crearTablero():
    return [0 for i in range(9)]

def marcar(tablero, posicion, jugador):
    if tablero[posicion] == 0:
        tablero[posicion] == jugador
    else:
        marcar(tablero, posicion, jugador)
    return tablero

def revisarTablero(tablero):
    posicionesDeVictorias = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 7],
        [2, 4, 6]
    ]
    for posiciones in posicionesDeVictorias: #Revisar que un jugador haya marcado alguna de las posciones
        if tablero[posiciones][0] == tablero[posiciones][1] and tablero[posiciones][1] == tablero[posiciones][2]:
            return tablero[posiciones][0]
    return None


def mostrarTablero(tablero):
    for i in range(9):
        casilla= tablero[i]
        if casilla == 1:
            print("o", end= " ")
        elif casilla == -1:
            print("x", end= " ")
        else:
            print(" ", end= " ")
        if(i+1) % 3 == 0: #Crear el salto de línea en el triqui
            print()
        
continuar = True

while continuar:
    print("Menu de opciones")
    print("1.Jugar contra una máquina")
    print("2.Jugar con otra persona")
    print("\n0. Salir")

    opcion = leerOpcion()
    match opcion:
        case 0:
            continuar = False
            print("¡Gracias por jugar!")
            break
        case 1: 
            break
        case 2:
            break


