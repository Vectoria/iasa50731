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
        Erro na semana 8, no qual adcionava o nó no inicio da lista ao inves no fim, uma vez que 
        o raciocinio do lifo e fifo não tinha em conta que a eliminação do nó era no primeiro indice,
        corrigido no dia 22 de maio

        Args:
            no (No): nó que vai ser inserido
        """
        self._nos.append(no)
