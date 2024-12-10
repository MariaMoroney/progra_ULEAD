from calculador_impuesto import impuestoCalculator 

class OrdenDeCompra:
    def __init__(self, productos):
        self._productos = productos
    
    def get_productos(self):
        return self._productos
    
    def listar_productos(self):
        return [producto.get_nombre() for producto in self._productos]
    
    def calcular_precio_final(self, estado):
        # Validacion de estado
        if not impuestoCalculator.es_estado_valido(estado):
            raise ValueError(f"Estado {estado} no es válido")
        
        # Calcular subtotal
        subtotal = sum(producto.get_precio() for producto in self._productos)
        
        # Calcular impuestos
        impuestos = impuestoCalculator.calcular_impuestos(subtotal, estado)
        
        # Precio final = subtotal + impuestos
        return subtotal + impuestos
    