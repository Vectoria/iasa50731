from abc import ABC, abstractmethod


class Operador(ABC):
    """
    Baixo acoplamento, uma vez que só tem dependencias

    A classe é interface, contrato funcional,
    do qual as classes que implementarem esta interface, podem escolher o melhor criterio para o operador para
    a sua respectiva finalidade

    Representa uma ação, uma mundança de um estado existente para um novo, em que podem chegar ao objetivo

    O oposto de um operador é um antecessor

    Args:
        ABC (ABC): torna em uma interface
    """
    @abstractmethod
    def aplicar(self, estado):
        """ gera, usando o operador, um estado sucessivo """

    @abstractmethod
    def custo(self, estado, estado_suc):
        """ o custo para o proximo estado """
