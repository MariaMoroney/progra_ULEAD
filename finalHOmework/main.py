from producto import Producto
from ordenDeCompra import OrdenDeCompra

# Crear algunos productos
producto1 = Producto("Espejo", "ESP001", 1000)
producto2 = Producto("Celular", "CEL002", 2000)
producto3 = Producto("Silla", "SIL003", 100)

# Crear una orden de compra
orden = OrdenDeCompra([producto1, producto2, producto3])

# Probar cálculo de precio final para diferentes estados
try:
    # Estado con impuesto fijo
    precio_TX = orden.calcular_precio_final('TX')
    print(f"Precio final en TX: ${precio_TX:.2f}")

    # Estado sin impuestos
    precio_MA = orden.calcular_precio_final('MA')
    print(f"Precio final en MA: ${precio_MA:.2f}")

    # Estado con impuesto escalonado
    precio_il = orden.calcular_precio_final('IL')
    print(f"Precio final en IL: ${precio_il:.2f}")

except ValueError as e: 
    print(e)