from libro import Libro
from usuario import Usuario
from json_handler import BibliotecaJSONHandler

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.json_handler = BibliotecaJSONHandler()

    def inicializar(self):
        """Cargar datos al iniciar la biblioteca"""
        try:
            self.json_handler.cargar_biblioteca(self)
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            # Continuar con una biblioteca vacía si hay error

    def guardar(self):
        """Guardar datos de la biblioteca"""
        try:
            self.json_handler.guardar_biblioteca(self)
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def agregar_libro(self, libro):
        """Agregar un libro a la biblioteca"""
        self.libros.append(libro)
        self.guardar()

    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario"""
        if any(u.id_usuario == usuario.id_usuario for u in self.usuarios):
            raise ValueError(f"Ya existe un usuario con el ID {usuario.id_usuario}")
        self.usuarios.append(usuario)
        self.guardar()

    def prestar_libro(self, titulo, id_usuario):
        """Prestar un libro a un usuario"""
        libro = next((l for l in self.libros 
                     if l.titulo.lower() == titulo.lower() and l.disponible), None)
        if not libro:
            raise ValueError(f"Libro '{titulo}' no disponible")

        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            raise ValueError(f"Usuario con ID {id_usuario} no encontrado")

        libro.disponible = False
        usuario.libros_prestados.append(libro)
        self.guardar()

    def devolver_libro(self, titulo, id_usuario):
        """Devolver un libro prestado"""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            raise ValueError(f"Usuario con ID {id_usuario} no encontrado")

        libro = next((l for l in usuario.libros_prestados 
                     if l.titulo.lower() == titulo.lower()), None)
        if not libro:
            raise ValueError(f"El libro '{titulo}' no está prestado a este usuario")

        libro.disponible = True
        usuario.libros_prestados.remove(libro)
        self.guardar()

    def mostrar_libros_disponibles(self):
        """Mostrar lista de libros disponibles"""
        return [libro for libro in self.libros if libro.disponible]

    def mostrar_usuarios(self):
        """Mostrar lista de usuarios"""
        return self.usuarios