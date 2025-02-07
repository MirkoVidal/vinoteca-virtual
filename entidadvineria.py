from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    @abstractmethod
    def __init__(self, id, nombre: str):
        self._id = id
        self._nombre = nombre
    
    def establecerNombre(self, nombre: str):
        self._nombre = nombre
        
    def obtenerNombre(self) -> str:
        return self._nombre
    
    def obtenerId(self) -> str:
        return self._id

    def equals(self, e):
        if isinstance(e, EntidadVineria):
            return self._id == e.obtenerId()
        else:
            return False