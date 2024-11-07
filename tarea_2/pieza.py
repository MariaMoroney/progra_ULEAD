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