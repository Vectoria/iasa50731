from abc import ABC, abstractmethod


class ModeloPlan(ABC):
    """
    Consiste em um modelo plano, que pode ser modelo mundo (representação interna do ambiente) ou
    ModeloPDMPlan

    Args:
        ABC (ABC): interface
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
