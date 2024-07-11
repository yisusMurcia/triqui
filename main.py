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
        tablero[posicion] = jugador
    else:
        marcar(tablero, posicion, jugador)
    return tablero

def seleccionarPosicion(tablero):
    posicionValida = False
    while not posicionValida:
        posicion = input("Ingrese la posicion que quiere marcar: ")
        if posicion in "123456789":
            posicion = int(posicion) - 1
            if tablero[posicion] == 0: #Revisar que no este marcado
                posicionValida = True
    return posicion

def revisarTablero(tablero):
    if 0 not in tablero:#Revisar posible empate
        return 0
    posicionesDeVictorias = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for posiciones in posicionesDeVictorias: #Revisar que un jugador haya marcado alguna de las posciones
        if tablero[posiciones[0]] == 0:
            continue
        if tablero[posiciones[0]] == tablero[posiciones[1]] and tablero[posiciones[1]] == tablero[posiciones[2]]:
            return tablero[posiciones[0]]
    return None


def mostrarTablero(tablero):
    for i in range(9):
        casilla= tablero[i]
        if casilla == 1:
            opcion = "o"
        elif casilla == -1:
            opcion = "x"
        else:
            opcion = " "
        if(i+1) % 3 == 0: #Crear el salto de línea en el triqui
            print(f"{opcion}\n{i-1} {i} {i+1}\n")
        else:
            print(opcion + "|", end= "")

def minMax(tablero, jugador, iteraciones = 0):#Evaluar posibles movimientos
    movimientos = []
    print(iteraciones)
    #Devolver numeros cuando se haya ganado o haya empate
    if revisarTablero(tablero) != None and iteraciones != 0:
        return [revisarTablero(tablero)]

    for i in range(0, len(tablero)):
        if tablero[i] == 0:
            copiaTablero = tablero[:]
            copiaTablero[i] = jugador
            puntuacion = minMax(copiaTablero, jugador*(-1), iteraciones +1)
            movimientos.append([puntuacion[0], i])
    
    #Retornar el movimiento más oportuno
    movimientos.sort(key= lambda x: x[0])
    if jugador == 1:
        movimientos.reverse()
    return movimientos[0]

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
            print("Juego contra máquina")
            tablero = crearTablero()
            jugador = -1
            mostrarTablero(tablero)

            while revisarTablero(tablero) == None:
                #Solicitar jugada en caso de turno del jugador
                if jugador == -1:
                    posicion = seleccionarPosicion(tablero)
                else:
                    puntuacion = minMax(tablero, jugador)
                    posicion = puntuacion[1]
                    print(f"la maquina marca {posicion}")
                tablero = marcar(tablero, posicion, jugador)
                mostrarTablero(tablero)
                jugador *= -1
            if revisarTablero(tablero) != 0:
                print("¡Triqui!")
                print(f"{"Ganaste" if jugador == 1 else "perdiste"}")
            else:
                print("Vaya, es un empate")
        case 2:
            tablero = crearTablero()
            jugador = 1
            mostrarTablero(tablero)

            while not revisarTablero(tablero):
                posicion = seleccionarPosicion(tablero)
                tablero = marcar(tablero, posicion, jugador)
                mostrarTablero(tablero)
                jugador*= -1 #Cambiar de turno
            if revisarTablero(tablero) == 0:
                print("Vaya, es un empate")
            elif revisarTablero(tablero) != None:
                print("¡Triqui!")
                print(f"El ganador es: {"o" if jugador == -1 else "x"}")


