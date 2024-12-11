class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def to_dict(self):
        """Convertir usuario a diccionario para JSON"""
        return {
            'nombre': self.nombre,
            'id_usuario': self.id_usuario,
            'libros_prestados': [libro.consecutivo for libro in self.libros_prestados]
        }

    @classmethod
    def from_dict(cls, data, libros):
        """Crear usuario desde diccionario JSON"""
        usuario = cls(data['nombre'], data['id_usuario'])
        # Asociar libros prestados usando los consecutivos
        for consecutivo in data['libros_prestados']:
            libro = next((l for l in libros if l.consecutivo == consecutivo), None)
            if libro:
                usuario.libros_prestados.append(libro)
        return usuario

