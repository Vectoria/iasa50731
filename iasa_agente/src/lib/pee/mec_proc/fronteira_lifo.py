from .fronteira import Fronteira


class FronteiraLIFO(Fronteira):
    """
    Fronteira que o recebe um item no fim e elimina o primeiro

    Quando implementado pela estrutura de dados, tem o conceito de "Stack",
    já que o primeiro inserido, será o ultimo a sair, como uma pilha de caixas

    Args:
        Fronteira (Fronteira): extend
    """

    def inserir(self, no):
        """
        faz o inseramento do nó da fronteira, no caso, no fim da lista dos nós

        contia um erro na entrega da entrega 7, onde eliminava o ultimo nó

        Args:
            no (No): nó que vai ser inserido
        """
        self._nos.append(no)
