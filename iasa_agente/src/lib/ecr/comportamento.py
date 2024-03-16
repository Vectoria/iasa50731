"""
    Para aplicar a interface
"""
from abc import ABC, abstractclassmethod

class Comportamento(ABC):
    """
    Comportamento é uma interface, ou seja, contrato funcional
    Pode existir escalar para dois tipos de comportamento:
    o simples (reação) ou o comportamento composto (conjunto de comportamentos agregados)

    """    

    @abstractclassmethod
    def activar(self,percepcao):
        """
        a classe recebe o ABC para transformar em abstracto/interface
        de seguida, em cada classe que ainda n foi implementado, escrevemos um @abstractclassmethod
        e escrevemos no metodo uma string, de maneira a não dar erro (como um raise NotImplementedError) """
        "Ação"