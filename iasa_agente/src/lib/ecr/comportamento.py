from abc import ABC, abstractclassmethod

class Comportamento(ABC):
    """
    Comportamento é uma interface funcional

    """    

    @abstractclassmethod
    def activar(self,percepcao):
        """
        a classe recebe o ABC para transformar em abstracto/interface
        de seguida, em cada classe que ainda n foi implementado, escrevemos um @abstractclassmethod
        e escrevemos no metodo uma string, de maneira a não dar erro (como um raise NotImplementedError) """
        "Ação"