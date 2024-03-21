from ecr.hierarquia import Hierarquia
from .explorar.explorar import Explorar
from .aproximar.aproximar_alvo import AproximarAlvo
from .evitar.evitar_obstaculos import EvitarObst

class Recolher(Hierarquia):
    """
    O recolher é uma hierarquia, por este ter uma lista de comportamentos
    É representação do diagrama informal, onde tem mais prioridade nos níveis de competência:
    aproximar, de seguida pelo evitar e por fim pelo explorar.

    Como só temos a classe Explorar implementada e as outras não, só teremos este na lista de comportamentos

    Acoplamento alto, devido ao extend, contém uma fatorização estrutural
    Args:
        Hierarquia (Hierarquia): extende
    """    
   # __comportamentos=[AproximarAlvo(),EvitarObst(),Explorar()]
    __comportamentos=[Explorar()]
    def __init__(self):
        """
        factorização, usa a classe dos comportamentos compostos para ser incializado,
        introduzindo os comportamentos
        """        
        super().__init__(self.__comportamentos)