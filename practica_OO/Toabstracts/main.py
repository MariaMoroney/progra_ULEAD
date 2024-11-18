from tablero import Tablero
from transformador_xml import TransformadorXML

# Crear un tablero de 3x3
tablero = Tablero(8, 8)
print("Tablero:\n", tablero)

# Crear un objeto de TransformadorXML
transformador = TransformadorXML()

# Suponiendo que el tablero tiene algunos atributos privados, como:
tablero._Tablero__atributo_privado = "Nuevo valor privado"

# Serializar el objeto tablero a XML
xml = transformador.serialize(tablero)
print("\nXML del objeto:\n", xml)