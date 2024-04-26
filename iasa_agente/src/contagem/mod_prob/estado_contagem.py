
from mod.estado import Estado


class EstadoContagem(Estado):
    """
    O estado cujo o valor é númerico
    Args:
        Estado (Estado): extende
    """

    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def id_valor(self):
        return hash(self.__valor)
