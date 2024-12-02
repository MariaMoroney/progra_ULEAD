from frecuency_counter import frecuency_counter

filename = input("Enter the name of the file: ")
frecuency = frecuency_counter(filename)

if frecuency is not None:
          print("letter frequecies")
          for key, value in sorted(frecuency.items()):
                  print(f"{key}: {value}")
          else:
                  print("error: file could not be opened")