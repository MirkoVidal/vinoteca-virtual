import json
from entidadvineria import EntidadVineria
import vinoteca

class Cepa(EntidadVineria):
    def __init__(self, id, nombre: str):
        super().__init__(id, nombre)
    
    def obtenerVinos(self):
        return [vino for vino in vinoteca.Vinoteca.obtenerVinos() if self in vino.obtenerCepas()]

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre() + " ("+ a.obtenerBodega().obtenerNombre()+ ")", vinos)
        return list(vinosMapa)