from abc import ABC, abstractmethod


class Estado(ABC):

    @abstractmethod
    def id_valor(self):
        """ fixe """

    def __hash__(self):
        """gera um inteiro unico para representar a indentificação de uma instancia da classe
        """
        return self.id_valor()

    def __eq__(self, other):
        """
        Para comparar o hash da classe atual com outra instancia e ver se são iguais

        Returns:
            bool: _description_
        """
        if isinstance(other, Estado):
            return self.__hash__ == other.__hash__
