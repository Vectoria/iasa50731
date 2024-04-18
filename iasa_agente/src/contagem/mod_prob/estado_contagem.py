
from mod.estado import Estado


class EstadoContagem(Estado):
    """
    Classe que representa o estado do problema que o professor 
    falou no dia 18 de abril, 8 semana

    Neste caso, consiste em que o estado é um valor númerico
    Args:
        Estado (_type_): extende
    """

    def __init__(self, valor):
        self.__valor = valor
        pass

    @property
    def valor(self):
        return self.__valor

    def id_valor(self):
        return hash(self.__valor)
