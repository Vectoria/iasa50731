from abc import ABC, abstractmethod


class Plano(ABC):
    """
    uma interface (encapsulamento) onde a sua essencia é ser um plano de ação, gerando ação

    Args:
        ABC (ABC): interface
    """
    @abstractmethod
    def obter_accao(self, estado):
        """ obtem-se a ação """
    @abstractmethod
    def mostrar(self, vista):
        """ mostra """
