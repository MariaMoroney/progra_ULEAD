from ficha_base import Ficha

class FichaGris(Ficha):
    """Clase para fichas grises del jugador 2."""
    def _init_(self):
        super()._init_("G")