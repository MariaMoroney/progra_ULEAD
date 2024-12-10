import utilidades

if __name__ == "__main__":
    # Test de read_int
    try:
        numero = utilidades.read_int(prompt="Ingrese un número entero: ", qty_attempts=3, only_positives=True)
        print(f"El número entero ingresado es: {numero}")
    except Exception as e:
        print(e)

    # Test de read_floating_point
    try:
        numero_float = utilidades.read_floating_point(prompt="Ingrese un número decimal: ", qty_attempts=3, only_positives=True)
        print(f"El número decimal ingresado es: {numero_float}")
    except Exception as e:
        print(e)

    # Test de get_file
    try:
        archivo = utilidades.get_file("archivo_prueba.txt", end_program=False)
        print("Archivo abierto correctamente.")
        archivo.close()
    except Exception as e:
        print(e)

    # Test de display_menu
    opciones = ["Opción 1", "Opción 2", "Opción 3"]
    utilidades.display_menu(titulo_menu="Mi Menú", lista_opciones=opciones, caracter_opciones="alfabético")
