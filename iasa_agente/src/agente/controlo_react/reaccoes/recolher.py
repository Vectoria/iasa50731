from ecr.hierarquia import Hierarquia
from .explorar.explorar import Explorar
from .explorar.explorar_rodar import ExplorarRodar
from .aproximar.aproximar_alvo import AproximarAlvo
from .evitar.evitar_obstaculos import EvitarObst


class Recolher(Hierarquia):
    """
    O recolher é uma hierarquia, ou seja, contém uma lista de comportamentos
    É representação do diagrama informal (slide 10), onde há comportamentos com mais prioridade nos níveis de competência:
    aproximar, de seguida pelo evitar e por fim pelo explorar.

    Como inicialmente só tinhamos a classe Explorar implementada e as outras não, só teremos este na lista de comportamentos, 
    atualmente já possui todos os comportamnetos

    Acoplamento alto, devido ao extend, contém uma fatorização estrutural
    Args:
        Hierarquia (Hierarquia): extende
    """
    __comportamentos = [AproximarAlvo(), EvitarObst(), Explorar()]
    # __comportamentos=[Explorar()]
    # __comportamentos=[AproximarAlvo(),Explorar()]

    def __init__(self):
        """
        factorização, usa a classe dos comportamentos compostos para ser incializado,
        introduzindo os comportamentos
        """
        super().__init__(self.__comportamentos)
