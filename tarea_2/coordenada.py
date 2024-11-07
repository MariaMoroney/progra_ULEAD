# Clase Coordenada para manejar las posiciones en el tablero
class Coordenada:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def __eq__(self, otra):
        return isinstance(otra, Coordenada) and self.fila == otra.fila and self.columna == otra.columna

    def __str__(self):
        return f"{chr(self.columna + ord('a'))}{self.fila + 1}"

    @staticmethod
    def from_str(casilla):
        columna = ord(casilla[0].lower()) - ord('a')
        fila = int(casilla[1]) - 1
        return Coordenada(fila, columna)