from abc import ABC, abstractmethod


class Plano(ABC):
    @abstractmethod
    def obter_accao(self, estado):
        """ obtem-se a ação """
    @abstractmethod
    def mostrar(self, vista):
        """ mostra """
