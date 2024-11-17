from persona import Persona

una_persona = Persona("Fernando", 111)

for att in una_persona.__dict__:
          print("<" + att + ">" "un valor" + "<" + att + ">")