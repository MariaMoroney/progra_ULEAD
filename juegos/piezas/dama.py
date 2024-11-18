from juegos.piezas.ficha_base import Ficha

class Dama(Ficha):
    """Clase para las fichas promovidas a damas."""
    def _init_(self, color):
        super()._init_(color.upper())  # "R" -> "DR" o "G" -> "DG"

    def es_dama(self):
        """Indica que esta ficha es una dama."""
        return True

