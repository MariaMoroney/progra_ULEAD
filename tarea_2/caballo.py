from coordenada import Coordenada
from pieza import Pieza

class Caballo(Pieza):
    def mover(self, casilla_destino):
        destino = Coordenada.from_str(casilla_destino)
        movimientos = [
            Coordenada(self.posicion.fila + 2, self.posicion.columna + 1),
            Coordenada(self.posicion.fila + 2, self.posicion.columna - 1),
            Coordenada(self.posicion.fila - 2, self.posicion.columna + 1),
            Coordenada(self.posicion.fila - 2, self.posicion.columna - 1),
            Coordenada(self.posicion.fila + 1, self.posicion.columna + 2),
            Coordenada(self.posicion.fila + 1, self.posicion.columna - 2),
            Coordenada(self.posicion.fila - 1, self.posicion.columna + 2),
            Coordenada(self.posicion.fila - 1, self.posicion.columna - 2)
        ]
        return destino in movimientos