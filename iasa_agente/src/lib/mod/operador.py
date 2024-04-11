from abc import ABC, abstractclassmethod


class Operador(ABC):
    @abstractclassmethod
    def aplicar(self, estado):
        """ gera, usando o operador, um estado sucessivo """

    @abstractclassmethod
    def custo(self, estado, estado_suc):
        """ o custo para o proximo estado """
