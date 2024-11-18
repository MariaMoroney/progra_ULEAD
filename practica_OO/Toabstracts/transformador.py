from abc import ABC, abstractmethod

class Transformador(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass  # Método abstracto, no hace nada por sí mismo