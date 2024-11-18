from transformador import Transformador

class TransformadorXML(Transformador):
    def serialize(self, obj):
        # Inicia el string XML
        xml_string = "<objeto>\n"

        # Recorre los atributos privados del objeto
        for key, value in obj.__dict__.items():
            if key.startswith("_") and not key.startswith("__"):  # Solo atributos privados
                xml_string += f"  <{key}>{value}</{key}>\n"

        xml_string += "</objeto>"
        return xml_string
