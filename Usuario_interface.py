from abc import ABC, abstractmethod
from Usuario import Usuario

# Creacion de una clase abstracta para evitar 
# O- Open closed
# L - Sustitución de Liskov
class Usuario_interface(ABC):
    @abstractmethod
    def get_Tuple_Data(self):
        pass