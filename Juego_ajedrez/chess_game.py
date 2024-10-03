# Aqui va el juego


def main():
    opcion = None
    while opcion != "3":
        imprimir_menu()
        opcion = input("Escoja una opcion:\n")
        evaluar_opcion(opcion)

def imprimir_menu():
    print("Escoja la opcion:")
    print("1. Posicion estandard inicial")
    print("2. Posicion inventada")
    print("3. Salir")

def evaluar_opcion(opcion):
    if opcion == "1":
        poner_tablero_estandard()
    elif opcion == "2":
        poner_tablero_inventado()

def poner_tablero_estandard():
    print("poniendo posicion inicial")
    jugar_posicion("b")

def poner_tablero_inventado():
    color = None
    while color != "fin":
        print("Escriba el color de la pieza (b/n), o 'fin' para empezar a jugar\n")
        color = input()
        if color != "fin":
            pieza = leer_pieza()
            casilla = leer_casilla()
            insertar_en_tablero(color, pieza, casilla)
    print("¿A cuál bando le toca jugar? (b/n)\n")
    bando_jugador = input()
    jugar_posicion(bando_jugador)

def jugar_posicion(color):
    jugada = None
    while jugada != "fin":
        jugada = input("Escriba la jugada a realizar (escriba 'print' para ver el tablero, 'fin' para terminar)\n")
        if jugada == "print":
            imprimir_tablero()
        elif jugada != "fin":
            print("Aquí iría el método de evaluación-validación")
            print("Ejecutar la jugada")

def imprimir_tablero():
    tablero = [[" "," "," "," "," "," "," "," "],
               [" "," ",7,7,7,7,7,7],
               [6,6,6,6,6,6,6,6],
               [5,5,5,5,5,5,5,5],
               [4,4,4,4,4,4,4,4],
               [3,3,3,3,3,3,3,3],
               [2,2,2,2,2,2,2,2],
               [1,1,1,1,1,1,1,1]]
    for fila in tablero:
        for casilla in fila:
            print(f"| {casilla} |", end="")
        print("\n")

def leer_pieza():
    pieza = None
    piezas_validas = ["R", "N", "B", "Q", "K", "P"]
    while pieza not in piezas_validas:
        print("Escriba la pieza a colocar (R=torre, N=caballo, B=alfil, Q=reina, K=rey, P=peón):")
        pieza = input().upper()
        if pieza not in piezas_validas:
            print("Pieza no válida, intente de nuevo.")
    return pieza

def leer_casilla():
    casilla = None
    columnas = "abcdefgh"
    filas = "12345678"
    while not casilla or len(casilla) != 2 or casilla[0] not in columnas or casilla[1] not in filas:
        print("Escriba la casilla (ejemplo: e2):")
        casilla = input().lower()
        if len(casilla) != 2 or casilla[0] not in columnas or casilla[1] not in filas:
            print("Casilla no válida, intente de nuevo.")
    return casilla

def insertar_en_tablero(color, pieza, casilla):
    print(f"Insertando la pieza {pieza} de color {color} en la casilla {casilla}")

if __name__ == "__main__":
    main()