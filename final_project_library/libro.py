class Libro:
    _contador_libros = 0

    def __init__(self, titulo, autor, anio_publicacion, numero_de_volumen):
        Libro._contador_libros += 1
        self.consecutivo = Libro._contador_libros
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True
        self.numero_de_volumen = numero_de_volumen

    def __str__(self):
        return f"Libro: {self.titulo} (Vol. {self.numero_de_volumen}) - Autor: {self.autor}, Año: {self.anio_publicacion}"

    def to_dict(self):
        """Convertir libro a diccionario para JSON"""
        return {
            'consecutivo': self.consecutivo,
            'titulo': self.titulo,
            'autor': self.autor,
            'anio_publicacion': self.anio_publicacion,
            'disponible': self.disponible,
            'numero_de_volumen': self.numero_de_volumen
        }

    @classmethod
    def from_dict(cls, data):
        """Crear libro desde diccionario JSON"""
        libro = cls(
            data['titulo'],
            data['autor'],
            data['anio_publicacion'],
            data['numero_de_volumen']
        )
        libro.consecutivo = data['consecutivo']
        libro.disponible = data['disponible']
        return libro