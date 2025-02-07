import json
from entidadvineria import EntidadVineria
from modelos.bodega import Bodega
from modelos.cepa import Cepa
import vinoteca

class Vino(EntidadVineria):
    def __init__(self, id, nombre: str, bodega: str, cepas: list[str], partidas: list[int]):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas
        
    def establecerBodega(self, bodega: str):
        self.__bodega = bodega
        
    def establecerCepas(self, cepas: list[str]):
        self.__cepas = cepas
        
    def establecerPartidas(self, partidas: list[int]):
        self.__partidas = partidas
        
    def obtenerBodega(self) -> Bodega:
        return vinoteca.Vinoteca.buscarBodega(self.__bodega)
    
    def obtenerCepas(self) -> list[Cepa]:
        cepas = []
        for cepaID in self.__cepas:
            cepa = vinoteca.Vinoteca.buscarCepa(cepaID)
            if cepa:
                cepas.append(cepa)
        return cepas
        
    def obtenerPartidas(self) -> list[int]:
        return self.__partidas

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self) -> dict:
        bodega = self.obtenerBodega()
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": bodega.obtenerNombre() if bodega else "No se encontro la bodega",
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self) -> dict:
        bodega = self.obtenerBodega()
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": bodega.obtenerNombre() if bodega else "No se encontro la bodega",
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
