# json_handler.py
import json
import os
from libro import Libro
from usuario import Usuario

class BibliotecaJSONHandler:
    def __init__(self, archivo_libros='libros.json', archivo_usuarios='usuarios.json'):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios

    def guardar_biblioteca(self, biblioteca):
        """Guardar toda la biblioteca en archivos JSON"""
        self.guardar_libros(biblioteca.libros)
        self.guardar_usuarios(biblioteca.usuarios)

    def guardar_libros(self, libros):
        """Guardar libros en archivo JSON"""
        libros_data = [libro.to_dict() for libro in libros]
        self._guardar_json(self.archivo_libros, libros_data)

    def guardar_usuarios(self, usuarios):
        """Guardar usuarios en archivo JSON"""
        usuarios_data = [usuario.to_dict() for usuario in usuarios]
        self._guardar_json(self.archivo_usuarios, usuarios_data)

    def cargar_biblioteca(self, biblioteca):
        """Cargar toda la biblioteca desde archivos JSON"""
        biblioteca.libros = self.cargar_libros()
        biblioteca.usuarios = self.cargar_usuarios(biblioteca.libros)

    def cargar_libros(self):
        """Cargar libros desde archivo JSON"""
        libros_data = self._cargar_json(self.archivo_libros)
        libros = []
        if libros_data:
            for libro_dict in libros_data:
                libro = Libro.from_dict(libro_dict)
                libros.append(libro)
                # Actualizar el contador de libros
                Libro._contador_libros = max(Libro._contador_libros, libro.consecutivo)
        return libros

    def cargar_usuarios(self, libros):
        """Cargar usuarios desde archivo JSON"""
        usuarios_data = self._cargar_json(self.archivo_usuarios)
        usuarios = []
        if usuarios_data:
            for usuario_dict in usuarios_data:
                usuario = Usuario.from_dict(usuario_dict, libros)
                usuarios.append(usuario)
        return usuarios

    def _guardar_json(self, archivo, datos):
        """Guardar datos en archivo JSON"""
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
        except Exception as e:
            raise Exception(f"Error al guardar en {archivo}: {str(e)}")

    def _cargar_json(self, archivo):
        """Cargar datos desde archivo JSON"""
        if not os.path.exists(archivo):
            return []
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error al cargar {archivo}: {str(e)}")