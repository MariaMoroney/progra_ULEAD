def frecuency_counter(filename):
          try:
                  file = open(filename)
                  text = file.read()
                  return {char: text.count(char) for char in text}
          except Exception as error:
                  print((f"Error: file could not be opened: {filename} ,{error}"))
                  return None
                  