from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

def menu_biblioteca():
    """Menú interactivo de la biblioteca"""
    biblioteca = Biblioteca()
    biblioteca.inicializar()

    while True:
        print("\n=== Biblioteca Virtual ===")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Ver libros disponibles")
        print("6. Ver usuarios")
        print("7. Salir")

        try:
            opcion = int(input("\nElija una opción (1-7): "))

            if opcion == 1:
                titulo = input("Título del libro: ")
                autor = input("Autor del libro: ")
                anio = int(input("Año de publicación: "))
                volumen = int(input("Número de volumen: "))
                libro = Libro(titulo, autor, anio, volumen)
                biblioteca.agregar_libro(libro)
                print("✓ Libro registrado exitosamente")

            elif opcion == 2:
                nombre = input("Nombre del usuario: ")
                while True:
                    try:
                        id_usuario = int(input("ID del usuario (número): "))
                        usuario = Usuario(nombre, id_usuario)
                        biblioteca.registrar_usuario(usuario)
                        print("✓ Usuario registrado exitosamente")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")

            elif opcion == 3:
                titulo = input("Título del libro a prestar: ")
                id_usuario = int(input("ID del usuario: "))
                biblioteca.prestar_libro(titulo, id_usuario)
                print("✓ Libro prestado exitosamente")

            elif opcion == 4:
                titulo = input("Título del libro a devolver: ")
                id_usuario = int(input("ID del usuario: "))
                biblioteca.devolver_libro(titulo, id_usuario)
                print("✓ Libro devuelto exitosamente")

            elif opcion == 5:
                libros = biblioteca.mostrar_libros_disponibles()
                if libros:
                    print("\nLibros disponibles:")
                    for libro in libros:
                        print(f"  • {libro}")
                else:
                    print("No hay libros disponibles")

            elif opcion == 6:
                usuarios = biblioteca.mostrar_usuarios()
                if usuarios:
                    print("\nUsuarios registrados:")
                    for usuario in usuarios:
                        print(f"\n  • {usuario}")
                        if usuario.libros_prestados:
                            print("    Libros prestados:")
                            for libro in usuario.libros_prestados:
                                print(f"      - {libro}")
                else:
                    print("No hay usuarios registrados")

            elif opcion == 7:
                biblioteca.guardar()
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida. Elija una opción entre 1 y 7.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    menu_biblioteca()