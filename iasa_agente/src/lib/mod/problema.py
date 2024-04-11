from abc import ABC, abstractclassmethod


class Problema(ABC):
    """
    Representa o dominio do problema, daquilo que estamos a resolver, transformamos no dominio interno 
    (computacional, dominio da logica) de maneira que chegamos ao objetivo 

    Args:
        ABC (ABC): método abstrado
    """

    def __init__(self, estado_inicial, operadores):
        """


        Args:
            estado_inicial (Estado): _description_
            operadores (Operador): _description_
        """
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
        pass

    @abstractclassmethod
    def objetivo(self, estado):
        """ o estado, ou conjunto de estados, que queremos antingir """

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
