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
 
