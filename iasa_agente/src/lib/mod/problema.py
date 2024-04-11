from abc import ABC, abstractclassmethod


class Problema(ABC):
    def __init__(self, estado_inicial, operadores):
        """

        Args:
            estado_inicial (_type_): _description_
            operadores (_type_): _description_
        """
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
        pass

    @abstractclassmethod
    def objetivo(self, estado):
        """ o estado que queremos antingir """

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
