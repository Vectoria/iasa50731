from abc import ABC, abstractclassmethod
class Comportamento(ABC):
    @abstractclassmethod
    def activar(self,percepcao):
        "Ação"