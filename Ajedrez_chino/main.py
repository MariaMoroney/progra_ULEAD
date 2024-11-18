from imprimir_tablero import imprimir_tablero
from c_tablero import crear_tablero
from movimiento import es_movimiento_valido
from mover_ficha import mover_ficha
from posicion import convertir_posicion

def main():
    try:
        tablero = crear_tablero()
        jugador = 1

        print("¡Bienvenido a Damas!")
        imprimir_tablero(tablero)

        while True:
            print(f"Turno del jugador {jugador} ({'R' if jugador == 1 else 'G'})")
            try:
                inicio = input("Introduce la posición de la ficha a mover (ej. A3): ").strip().upper()
                destino = input("Introduce la posición de destino (ej. B4): ").strip().upper()
                
                # Validar longitud mínima para evitar errores
                if len(inicio) < 2 or len(destino) < 2:
                    print("Posición inválida. Intenta de nuevo.")
                    continue
                
                inicio_idx = convertir_posicion(inicio)
                destino_idx = convertir_posicion(destino)

                # Validar si el movimiento es posible
                if es_movimiento_valido(tablero, inicio_idx, destino_idx, jugador):
                    print("True")  # Movimiento válido
                    mover_ficha(tablero, inicio_idx, destino_idx)
                    imprimir_tablero(tablero)
                    # Cambiar de jugador
                    jugador = 2 if jugador == 1 else 1
                else:
                    print("False")  # Movimiento inválido
            except (ValueError, IndexError):
                print("Entrada inválida. Asegúrate de introducir posiciones válidas (ej. A3, B4).")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

if __name__ == "__main__":
    main()