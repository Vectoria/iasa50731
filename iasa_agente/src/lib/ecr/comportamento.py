"""
    Para aplicar a interface importamos o ABC
"""
from abc import ABC, abstractclassmethod

class Comportamento(ABC):
    """
    Comportamento é uma interface (encapsulamento), ou seja, que é contrato funcional
    Consiste também no paradigma comportamental onde pode existir dois tipos de comportamento:
    o simples (reação) ou o comportamento composto (conjunto de comportamentos agregados)

    Além disso, possuí reactividade (uma caractrística dum agente inteligente)
    """    

    @abstractclassmethod
    def activar(self,percepcao):
        """
        Escrevemos um @abstractclassmethod ao método uma vez que é abstracto (como está no uml, slide 5), 
        escrevemos no metodo uma string, de maneira a não dar erro (como um raise NotImplementedError)

        Método que representa um modelo reactivo, e contém polimorfismo por parte das
        classes que implementarão este método
        """