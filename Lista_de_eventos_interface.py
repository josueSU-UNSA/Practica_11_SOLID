from abc import ABC, abstractmethod
from Lista_de_eventos import Lista_de_eventos

# Creacion de una clase abstracta para evitar 
# O- Open closed
class Lista_de_eventos_interface(ABC):
    @abstractmethod
    def agregar_evento(self,nuevoIdEvento):
        pass
    @abstractmethod
    def mostrarEventos(self):
        pass