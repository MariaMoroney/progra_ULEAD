from fichaRoja import FichaRoja
from fichaGris import FichaGris
from dama import Dama

class Ficha:
    """Clase base para las fichas."""
    def __init__(self, color):
        self.color = color  # "R" para rojas, "G" para grises

    def __str__(self):
        return self.color

    def es_dama(self):
        """Indica si la ficha es una dama (sobre-escrito en subclases)."""
        return False
    
class Tablero:
    """Clase que gestiona el tablero y los movimientos."""
    def __init__(self):
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        """Crea el tablero inicial de damas como una matriz 8x8."""
        tablero = [[None for _ in range(8)] for _ in range(8)]
        for fila in range(3):  # Fichas rojas (jugador 1)
            for col in range(8):
                if (fila + col) % 2 == 1:
                    tablero[fila][col] = FichaRoja()
        for fila in range(5, 8):  # Fichas grises (jugador 2)
            for col in range(8):
                if (fila + col) % 2 == 1:
                    tablero[fila][col] = FichaGris()
        return tablero

    def imprimir(self):
        """Imprime el tablero de forma visual."""
        print("  A B C D E F G H")
        for i, fila in enumerate(self.tablero):
            fila_str = []
            for casilla in fila:
                if casilla is None:
                    fila_str.append(" ")
                else:
                    fila_str.append(str(casilla))
            print(f"{i+1} " + " ".join(fila_str))
        print()

    @staticmethod
    def convertir_posicion(pos):
        """Convierte una posición en formato letra-número (ej. A3) a índices del tablero."""
        columna = ord(pos[0].upper()) - ord("A")
        fila = int(pos[1]) - 1
        return fila, columna

    def es_movimiento_valido(self, inicio, destino, jugador):
        """Verifica si un movimiento es válido."""
        fila_inicio, col_inicio = inicio
        fila_destino, col_destino = destino
        pieza = self.tablero[fila_inicio][col_inicio]

        if pieza is None:
            return False

        # Verificar si pertenece al jugador actual
        if (jugador == 1 and isinstance(pieza, FichaGris)) or (jugador == 2 and isinstance(pieza, FichaRoja)):
            return False

        # Movimiento simple diagonal (sin captura)
        direccion = 1 if jugador == 1 else -1
        if not pieza.es_dama():
            if abs(fila_destino - fila_inicio) == 1 and abs(col_destino - col_inicio) == 1:
                return fila_destino - fila_inicio == direccion and self.tablero[fila_destino][col_destino] is None

        # Movimiento de captura (salto)
        if abs(fila_destino - fila_inicio) == 2 and abs(col_destino - col_inicio) == 2:
            fila_salto = (fila_inicio + fila_destino) // 2
            col_salto = (col_inicio + col_destino) // 2
            ficha_saltada = self.tablero[fila_salto][col_salto]
            if ficha_saltada is not None and ficha_saltada.color != pieza.color:
                return self.tablero[fila_destino][col_destino] is None

        # Movimiento de la Dama: permite mover en cualquier dirección
        if pieza.es_dama():
            return abs(fila_destino - fila_inicio) == abs(col_destino - col_inicio) and self.tablero[fila_destino][col_destino] is None

        return False

    def mover_ficha(self, inicio, destino):
        """Mueve una ficha de una posición a otra y realiza capturas si es necesario."""
        fila_inicio, col_inicio = inicio
        fila_destino, col_destino = destino
        pieza = self.tablero[fila_inicio][col_inicio]

        # Si es un movimiento de captura
        if abs(fila_destino - fila_inicio) == 2:
            fila_salto = (fila_inicio + fila_destino) // 2
            col_salto = (col_inicio + col_destino) // 2
            self.tablero[fila_salto][col_salto] = None  # Eliminar ficha capturada

        # Promoción a dama
        if (fila_destino == 0 and isinstance(pieza, FichaRoja)) or (fila_destino == 7 and isinstance(pieza, FichaGris)):
            self.tablero[fila_destino][col_destino] = Dama(pieza.color)
        else:
            self.tablero[fila_destino][col_destino] = pieza

        self.tablero[fila_inicio][col_inicio] = None