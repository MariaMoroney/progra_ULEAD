def imprimir_tablero(tablero):
    """Imprime el tablero de forma visual."""
    print("  A B C D E F G H")
    for i, fila in enumerate(tablero):
        print(f"{i+1} " + " ".join(fila))
    print()