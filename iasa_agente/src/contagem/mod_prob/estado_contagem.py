
from mod.estado import Estado


class EstadoContagem(Estado):
    """
    O estado que é um valor númerico
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
