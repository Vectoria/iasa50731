from ecr.hierarquia import Hierarquia
from .explorar.explorar import Explorar
from .aproximar.aproximar_alvo import AproximarAlvo
from .evitar.evitar_obstaculos import EvitarObst

class Recolher(Hierarquia):
    """
    O recolher é uma hierarquia, por este ter uma lista de comportamentos

    Args:
        Hierarquia (Hierarquia): extende
    """    
   # __comportamentos=[AproximarAlvo(),EvitarObst(),Explorar()]
    __comportamentos=[Explorar()]
    def __init__(self):
        super().__init__(self.__comportamentos)