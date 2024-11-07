from coordenada import Coordenada
from pieza import Pieza

class Peon(Pieza):
    def mover(self, casilla_destino):
        destino = Coordenada.from_str(casilla_destino)
        if self.color == "blanco":
            movimientos = [Coordenada(self.posicion.fila + 1, self.posicion.columna)]
        else:
            movimientos = [Coordenada(self.posicion.fila - 1, self.posicion.columna)]
        return destino in movimientos