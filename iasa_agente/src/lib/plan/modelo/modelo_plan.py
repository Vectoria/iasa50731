from abc import ABC, abstractmethod


class ModeloPlan(ABC):
    """
    Documentar depois

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def obter_estado(self):
        """ obtem-se o estado """

    @abstractmethod
    def obter_estados(self):
        """ obtem-se os estados """

    @abstractmethod
    def obter_operadores(self):
        """ obtem-se os operadores """
