from abc import ABC, abstractmethod


class Operador(ABC):
    @abstractmethod
    def aplicar(self, estado):
        """ gera, usando o operador, um estado sucessivo """

    @abstractmethod
    def custo(self, estado, estado_suc):
        """ o custo para o proximo estado """
