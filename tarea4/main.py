import utilidades

def main():
    print("Read an integer")
    number = utilidades.get_integer_input(prompt="Please enter a number: ", max_attempts=3, positive_only=True)
    print(f"The number is {number}")

    print("Read a float")
    number = utilidades.get_float_input(prompt="Please enter a number: ", max_attempts=3, positive_only=True)
    print(f"The number is {number}")

    print("Open a file")
    file = utilidades.open_file()
    print(f"The file is {file}")

    print("Display a menu")
    utilidades.show_menu(menu_title="Menu", menu_options=["Option 1", "Option 2", "Option 3"])

if __name__ == "__main__":
    main()