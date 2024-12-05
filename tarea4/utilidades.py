def get_integer_input(prompt="Please enter a number: ", max_attempts=None, positive_only=False):
    attempt_count = 0
    while max_attempts is None or attempt_count < max_attempts:
        user_input = input(prompt)
        
        try:
            number = int(user_input)
            if positive_only and number < 0:
                print("Error: Only positive numbers are allowed.")
                attempt_count += 1
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid integer.")
            attempt_count += 1
    
    print("Error: Too many invalid attempts.")
    exit(1)


def get_float_input(prompt="Please enter a number: ", max_attempts=None, positive_only=False):
    attempt_count = 0
    while max_attempts is None or attempt_count < max_attempts:
        user_input = input(prompt)
        
        try:
            number = float(user_input)
            if positive_only and number < 0:
                print("Error: Only positive numbers are allowed.")
                attempt_count += 1
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid floating-point number.")
            attempt_count += 1
    
    print("Error: Too many invalid attempts.")
    exit(1)

def open_file():
    file_path = input("Please enter the file path: ")

    if not file_path.endswith(".txt"):
        print("Error: Only .txt files are allowed.")
        exit(1)

    try:
        return open(file_path, "r")
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)

def show_menu(menu_title="Menu", menu_options=None):
    if not menu_options:
        print("No options available.")
        return
    
    print(menu_title)
    print("=" * len(menu_title))
    
    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")
    
    print()