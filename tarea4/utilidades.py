def read_int(prompt="Introduzca el número: ", qty_attempts=None, only_positives=False):
    attempts = 0
    while qty_attempts is None or attempts < qty_attempts:
        try:
            user_input = input(prompt)
            number = int(user_input)
            if only_positives and number < 0:
                print("El número no puede ser negativo.")
                attempts += 1
                continue
            return number
        except ValueError:
            print("Entrada inválida. Por favor, introduzca un número entero.")
            attempts += 1
    raise Exception("Cantidad máxima de intentos alcanzada.")

def read_floating_point(prompt="Introduzca el número: ", qty_attempts=None, only_positives=False):
    attempts = 0
    while qty_attempts is None or attempts < qty_attempts:
        try:
            user_input = input(prompt)
            number = float(user_input)
            if only_positives and number < 0:
                print("El número no puede ser negativo.")
                attempts += 1
                continue
            return number
        except ValueError:
            print("Entrada inválida. Por favor, introduzca un número con decimales.")
            attempts += 1
    raise Exception("Cantidad máxima de intentos alcanzada.")

def get_file(filename, end_program=True):
    try:
        return open(filename, 'r')
    except FileNotFoundError:
        with open("error.log", "a") as error_log:
            error_log.write(f"Archivo no encontrado: {filename}\n")
        if end_program:
            print("Archivo no existe. Terminando el programa.")
            exit()
        else:
            print("Archivo no existe. Por favor, introduzca otro archivo.")
            filename = input("Introduzca el nombre del archivo: ")
            try:
                return open(filename, 'r')
            except FileNotFoundError:
                print("Archivo no encontrado nuevamente. Terminando el programa.")
                exit()

def display_menu(titulo_menu="MENU", lista_opciones=None, caracter_opciones="numerado"):
    if lista_opciones is None:
        lista_opciones = []
    print(f"{titulo_menu}\n" + "-" * len(titulo_menu))
    for i, opcion in enumerate(lista_opciones):
        if caracter_opciones == "numerado":
            print(f"{i + 1}. {opcion}")
        else:
            print(f"{chr(97 + i)}. {opcion}")
