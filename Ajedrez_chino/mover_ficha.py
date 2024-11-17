def mover_ficha(tablero, inicio, destino):
    """Mueve una ficha de una posición a otra."""
    fila_inicio, col_inicio = inicio
    fila_destino, col_destino = destino
    tablero[fila_destino][col_destino] = tablero[fila_inicio][col_inicio]
    tablero[fila_inicio][col_inicio] = " "