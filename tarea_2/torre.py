from coordenada import Coordenada
from pieza import Pieza

class Torre(Pieza):
    def mover(self, casilla_destino):
        destino = Coordenada.from_str(casilla_destino)
        movimientos = []
        for i in range(1, 8):
            movimientos.extend([
                Coordenada(self.posicion.fila + i, self.posicion.columna),
                Coordenada(self.posicion.fila - i, self.posicion.columna),
                Coordenada(self.posicion.fila, self.posicion.columna + i),
                Coordenada(self.posicion.fila, self.posicion.columna - i)
            ])
        return destino in movimientos

