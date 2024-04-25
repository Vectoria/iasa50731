from .fronteira import Fronteira


class FronteiraFIFO(Fronteira):
    """
    Fronteira que o recebe um item no inicio e elimina o primeiro

    Quando implementado pela estrutura de dados, tem o conceito de "Queue",
    já que o primeiro a sair, será o primeiro a aparecer, como uma fila

    Args:
        Fronteira (Fronteira): extend
    """

    def inserir(self, no):
        """
        faz o inseramento do nó da fronteira, no caso, no inicio da lista dos nós

        contia um erro na entrega da entrega 7, onde eliminava o ultimo nó

        Args:
            no (No): nó que vai ser inserido
        """
        self.nos.insert(0, no)
