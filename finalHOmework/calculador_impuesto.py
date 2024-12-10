class impuestoCalculator:
    # Diccionario de estados con sus reglas de impuestos
    STATE_TAX_RULES = {
        'NH': {'rate': 0, 'description': 'Libre de impuestos'},
        'MA': {'rate': 0.18, 'description': 'Impuesto fijo 18%'},
        'CA': {'rate': 0.18, 'description': 'Impuesto fijo 18%'},
        'TX': {'rate': 0.18, 'description': 'Impuesto fijo 18%'},
        'IL': {
            'rate_low': 0, 
            'rate_mid': 0.12, 
            'rate_high': 0.16,
            'threshold_low': 1000,
            'threshold_high': 10000,
            'description': 'Impuesto escalonado'
        },
        'KY': {
            'rate_low': 0, 
            'rate_mid': 0.13, 
            'rate_high': 0.17,
            'threshold_low': 1000,
            'threshold_high': 10000,
            'description': 'Impuesto escalonado'
        }
    }

    @classmethod
    def calcular_impuestos(cls, total_compra, estado):
        """
        Calcula los impuestos según las reglas de cada estado
        
        Args:
            total_compra (float): Monto total de la compra
            estado (str): Código de estado de 2 letras
        
        Returns:
            float: Monto de impuestos
        
        Raises:
            ValueError: Si el estado no es válido
        """
        # Validar que el estado exista
        if estado.upper() not in cls.STATE_TAX_RULES:
            raise ValueError(f"Estado {estado} no es válido")
        
        # Obtener las reglas del estado
        rules = cls.STATE_TAX_RULES[estado.upper()]
        
        # Estados con impuesto fijo
        if 'rate' in rules:
            return total_compra * rules['rate']
        
        # Estados con impuesto escalonado (IL, KY)
        if total_compra < rules['threshold_low']:
            return 0
        elif total_compra < rules['threshold_high']:
            return total_compra * rules['rate_mid']
        else:
            return total_compra * rules['rate_high']

    @classmethod
    def es_estado_valido(cls, estado):
        """
        Verifica si un estado está en la lista de estados válidos
        
        Args:
            estado (str): Código de estado de 2 letras
        
        Returns:
            bool: True si el estado es válido, False en otro caso
        """
        return estado.upper() in cls.STATE_TAX_RULES

