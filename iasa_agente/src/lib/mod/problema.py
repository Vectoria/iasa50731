from abc import ABC, abstractmethod


class Problema(ABC):
    """
    Classe abstracta, contém forte acoplamento por extender

    Representa o dominio do problema, daquilo que estamos a resolver, onde transformamos o dominio interno para o do problema 
    (computacional, dominio da logica) de maneira que chegamos ao objetivo 

    Args:
        ABC (ABC): class abstrado
    """

    def __init__(self, estado_inicial, operadores):
        """
        No problema terá que começar por um estado inicial, e terá operadores, estes que são transição de estados 
        (representando como ações possiveis de chegar ao objetivo)

        Args:
            estado_inicial (Estado): Estado inicial para puder começar. Associação
            operadores (Operador): transição de estados (representando como ações possiveis de chegar ao objetivo). Associação
        """
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @abstractmethod
    def objetivo(self, estado):
        """o estado, ou conjunto de estados, que queremos antingir
         função do teste do objetivo 

        Args:
            estado (Estado): Estado que é o objetivo
        """

    @property
    def estado_inicial(self):
        """read-only
        """
        return self.__estado_inicial

    @property
    def operadores(self):
        """read-only
        """
        return self.__operadores
