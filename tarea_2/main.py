from dama import Dama
from peon import Peon
from caballo import Caballo
from rey import Rey
from torre import Torre
from alfil import Alfil

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


# Clase base para todas las piezas
class Pieza:
    def __init__(self, color, posicion):
        self.color = color
        self.posicion = posicion  # Tipo Coordenada

    def __eq__(self, otra):
        return isinstance(otra, type(self)) and self.color == otra.color and self.posicion == otra.posicion

    def __str__(self):
        return f"{type(self).__name__} {self.color} en {self.posicion}"

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_posicion(self, posicion):
        self.posicion = posicion

    def get_posicion(self):
        return self.posicion

    def mover(self, casilla_destino):
        # Este método será implementado en cada pieza específica
        pass

# Ejemplo de prueba
if __name__ == "__main__":
    peon_blanco = Peon("blanco", Coordenada(1, 4))  # Peón en e2
    print(peon_blanco)  # Output esperado: Peon blanco en e2
    print(peon_blanco.mover("e3"))  # Output esperado: True
    print(peon_blanco.mover("e4"))  # Output esperado: False

    dama_blanca = Dama("blanco", Coordenada(3, 3))  # Dama en d4
    print(dama_blanca)  # Output esperado: Dama blanco en d4
    print(dama_blanca.mover("g7"))  # Output esperado: True
    print(dama_blanca.mover("a1"))  # Output esperado: True

    caballo_blanco = Caballo("blanco", Coordenada(2, 3))  # Caballo en d4
    print(caballo_blanco)  # Output esperado: Caballo blanco en d4
    print(caballo_blanco.mover("e5"))  # Output esperado: True
    print(caballo_blanco.mover("a8"))  # Output esperado: True

    rey_blanco = Rey("blanco", Coordenada(1, 4))  # Rey en e2
    print(rey_blanco)  # Output esperado: Rey blanco en e2
    print(rey_blanco.mover("e3"))  # Output esperado: True
    print(rey_blanco.mover("e4"))  # Output esperado: False

    torre_blanca = Torre("blanco", Coordenada(3, 3))  # Torre en d4
    print(torre_blanca)  # Output esperado: Torre blanco en d4
    print(torre_blanca.mover("d2"))  # Output esperado: True
    print(torre_blanca.mover("d5"))  # Output esperado: True

    alfil_blanco = Alfil("blanco", Coordenada(1, 1))  # Alfil en d4
    print(alfil_blanco)  # Output esperado: Alfil blanco en d4
    print(alfil_blanco.mover("e5"))  # Output esperado: True
    print(alfil_blanco.mover("a8"))  # Output esperado: True

    peon_negro = Peon("negro", Coordenada(6, 4))  # Peón en e7
    print(peon_negro)  # Output esperado: Peón negro en e7
    print(peon_negro.mover("e6"))  # Output esperado: True
    print(peon_negro.mover("e5"))  # Output esperado: False

    dama_negra = Dama("negro", Coordenada(6, 3))  # Dama en d7
    print(dama_negra)  # Output esperado: Dama negra en d7
    print(dama_negra.mover("g4"))  # Output esperado: True
    print(dama_negra.mover("a8"))  # Output esperado: True

    caballo_negro = Caballo("negro", Coordenada(5, 3))  # Caballo en d7
    print(caballo_negro)  # Output esperado: Caballo negro en d7
    print(caballo_negro.mover("e6"))  # Output esperado: True
    print(caballo_negro.mover("a1"))  # Output esperado: True

    rey_negro = Rey("negro", Coordenada(6, 4))  # Rey en e7
    print(rey_negro)  # Output esperado: Rey negro en e7
    print(rey_negro.mover("e5"))  # Output esperado: True
    print(rey_negro.mover("e4"))  # Output esperado: False

    torre_negra = Torre("negro", Coordenada(6, 3))  # Torre en d7
    print(torre_negra)  # Output esperado: Torre negra en d7
    print(torre_negra.mover("d8"))  # Output esperado: True
    print(torre_negra.mover("d5"))  # Output esperado: True

    alfil_negro = Alfil("negro", Coordenada(5, 3))  # Alfil en d7
    print(alfil_negro)  # Output esperado: Alfil negro en d7
    print(alfil_negro.mover("e4"))  # Output esperado: True
    print(alfil_negro.mover("a1"))  # Output esperado: True

