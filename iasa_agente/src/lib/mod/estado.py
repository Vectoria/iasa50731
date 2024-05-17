from abc import ABC, abstractmethod


class Estado(ABC):
    """
    Acoplamento não existente

    Classe abstracta, representa uma configuração possível na resolução de um problema
    Cada estado tem a sua identificação apartir do seu hash, dessa forma é possível comparar 
    com outros estados

    Args:
        ABC (ABC): torna numa classe abstracta
    """
    @abstractmethod
    def id_valor(self):
        """ é o id do estado """

    def __hash__(self):
        """gera um inteiro unico para representar a indentificação de uma instancia da classe
        """
        return self.id_valor()

    def __eq__(self, other):
        """
        Para comparar o hash da classe atual com outra instancia e ver se são iguais

        Erro na semana 7, onde não possuia parenteses no hash, corrigido no dia 17 de maio

        Returns:
            bool: se é verdadeiro ou não a condição
        """
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()
