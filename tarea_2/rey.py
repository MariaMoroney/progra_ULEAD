from coordenada import Coordenada
from pieza import Pieza

class Rey(Pieza):
    def mover(self, casilla_destino):
        destino = Coordenada.from_str(casilla_destino)
        movimientos = [
            Coordenada(self.posicion.fila + 1, self.posicion.columna),
            Coordenada(self.posicion.fila - 1, self.posicion.columna),
            Coordenada(self.posicion.fila, self.posicion.columna + 1),
            Coordenada(self.posicion.fila, self.posicion.columna - 1),
            Coordenada(self.posicion.fila + 1, self.posicion.columna + 1),
            Coordenada(self.posicion.fila - 1, self.posicion.columna - 1),
            Coordenada(self.posicion.fila + 1, self.posicion.columna - 1),
            Coordenada(self.posicion.fila - 1, self.posicion.columna + 1)
        ]
        return destino in movimientos