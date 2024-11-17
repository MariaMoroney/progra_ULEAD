
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
