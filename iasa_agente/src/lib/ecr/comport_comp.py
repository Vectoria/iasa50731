from .comportamento import Comportamento
from abc import abstractmethod


class ComportComp(Comportamento):

    """
    Implementa a interface Comportamento,
    isso se da ao facto que é um comportamento composto

    Args:
        Comportamento (Comportamento): implementa a interface
    """

    def __init__(self, comportamentos):
        """
        agrega um conjunto de comportamentos

        Args:
            comportamentos (Comportamento): Agregação
        """
        self.__comportamentos = comportamentos

    def activar(self, percepcao):
        """
        Ativação do comportamento composto, onde percorremos todos os comportamentos existentes
        em que cria várias ações atráves de uma resposta aos estimulos gerados pela percepção, 
        depois de criar um aglomerado de ações, acontece a escolha da ação ideal

        Acontece uma delegação (factorização funcional) 

        Args:
            percepcao (Percepcao): para ativar os demais estimulos para 

        Returns:
            Accao: é a ação que foi respondida atráves de um mecanismo de seleção
            de ação
        """
        accoes = []
        for comp in self.__comportamentos:
            accao = comp.activar(percepcao)
            if accao is not None:
                accoes.append(accao)
        if accoes is not None:
            return self.selecionar_accao(accoes)

    @abstractmethod
    def selecionar_accao(self, accoes):
        """
        erro de que este método não era abstacto, corrigido no dia 28 de abril
        """
