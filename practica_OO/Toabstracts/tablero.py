class Tablero:
    def __init__(self, lineas, columnas):
        # Inicializa el tablero con las dimensiones dadas
        self.tablero = [[None for _ in range(columnas)] for _ in range(lineas)]
        # Atributo privado de ejemplo
        self.__atributo_privado = "Valor privado"

    def __str__(self):
        # Método para mostrar el tablero de manera legible
        return "\n".join([" ".join(["_" if espacio is None else str(espacio) for espacio in linea]) for linea in self.tablero])