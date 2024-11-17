def convertir_posicion(pos):
    """Convierte una posición en formato letra-número (ej. A3) a índices del tablero."""
    columna = ord(pos[0].upper()) - ord("A")
    fila = int(pos[1]) - 1
    return fila, columna