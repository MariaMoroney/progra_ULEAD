def crear_tablero():
    """Crea el tablero inicial de damas como una matriz 8x8."""
    tablero = [[" " for _ in range(8)] for _ in range(8)]
    for fila in range(3):  # Fichas rojas (jugador 1)
        for col in range(8):
            if (fila + col) % 2 == 1:
                tablero[fila][col] = "R"
    for fila in range(5, 8):  # Fichas grises (jugador 2)
        for col in range(8):
            if (fila + col) % 2 == 1:
                tablero[fila][col] = "G"
    return tablero

def imprimir_tablero(tablero):
    """Imprime el tablero de forma visual."""
    print("  A B C D E F G H")
    for i, fila in enumerate(tablero):
        print(f"{i+1} " + " ".join(fila))
    print()

def mover_ficha(tablero, inicio, destino):
    """Mueve una ficha de una posición a otra."""
    fila_inicio, col_inicio = inicio
    fila_destino, col_destino = destino
    tablero[fila_destino][col_destino] = tablero[fila_inicio][col_inicio]
    tablero[fila_inicio][col_inicio] = " "

def es_movimiento_valido(tablero, inicio, destino, jugador):
    """Verifica si un movimiento es válido según reglas básicas."""
    fila_inicio, col_inicio = inicio
    fila_destino, col_destino = destino
    pieza = tablero[fila_inicio][col_inicio]

    # Verificar que la casilla de destino esté vacía
    if tablero[fila_destino][col_destino] != " ":
        return False

    # Verificar que la pieza pertenece al jugador actual
    if (jugador == 1 and pieza != "R") or (jugador == 2 and pieza != "G"):
        return False

    # Verificar movimiento diagonal simple (sin captura)
    direccion = 1 if jugador == 1 else -1
    if abs(fila_destino - fila_inicio) == 1 and col_destino - col_inicio in [-1, 1]:
        return fila_destino - fila_inicio == direccion

    return False
 
def convertir_posicion(pos):
    """Convierte una posición en formato letra-número (ej. A3) a índices del tablero."""
    columna = ord(pos[0].upper()) - ord("A")
    fila = int(pos[1]) - 1
    return fila, columna