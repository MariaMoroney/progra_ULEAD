
# Representación inicial del tablero de ajedrez
initial_board = [
    ["T", "C", "A", "D", "R", "A", "C", "T"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["t", "c", "a", "d", "r", "a", "c", "t"]
]

# Función para imprimir el tablero
def print_board(board):
    print("  a b c d e f g h")
    print(" +----------------")
    for row in range(8):
        print(f"{row + 1}|", " ".join(board[8 - row - 1]), f"|{row + 1}")
    print(" +----------------")
    print("  a b c d e f g h")

# Función para configurar el tablero inicial
def reset_board():
    global initial_board
    board = [row[:] for row in initial_board]  # Copia el tablero inicial
    return board

# Función para configurar una posición "ad hoc"
def setup_custom_position():
    board = [[" " for _ in range(8)] for _ in range(8)]
    while True:
        pos = input("Ingresa la pieza y posición (Ej: Re5) o escribe 'FIN' para terminar: ").strip().lower()
        if pos == "fin":
            break
        elif len(pos) == 3:  # Ej: Re5
            piece, col, row = pos[0], pos[1], pos[2]
            x, y = 8 - int(row), ord(col) - ord('a')
            board[x][y] = piece
        else:
            print("Entrada no válida. Por favor usa el formato adecuado (Ej: Re5).")
    return board

# Función para validar jugadas (pendiente de implementar lógica de ajedrez)
def validate_move(move, board, turn):
    # Aquí se implementará la lógica para validar las jugadas
    pass

# Menú principal
def main():
    board = reset_board()
    while True:
        print("1. Posición inicial de partida de ajedrez")
        print("2. Posición 'ad hoc' por el usuario")
        print("3. Salir")
        choice = input("Selecciona una opción: ").strip()
        if choice == "1":
            board = reset_board()
            turn = "blancas"
        elif choice == "2":
            board = setup_custom_position()
            turn = input("¿De quién es el turno? (B/N): ").strip().lower()
            if turn == 'b':
                turn = "blancas"
            else:
                turn = "negras"
        elif choice == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")
            continue

        # Inicia el bucle de recepción de jugadas
        while True:
            action = input(f"Turno de {turn}. Ingresa tu jugada (o PRINT/FIN): ").strip().lower()
            if action == "fin":
                break
            elif action == "print":
                print_board(board)
            else:
                valid_move = validate_move(action, board, turn)
                if not valid_move:
                    print("Jugada no válida. Intenta de nuevo.")
                else:
                    # Actualiza el tablero (falta implementar)
                    pass

if __name__ == "__main__":
    main()