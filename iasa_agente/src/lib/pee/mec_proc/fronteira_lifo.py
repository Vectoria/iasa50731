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
        faz o inseramento do nó da fronteira, no caso, no inicio da lista que sofrera shift

        contia um erro na entrega da entrega 7, onde eliminava o ultimo nó
        Erro na semana 8, no qual adcionava o nó no fim da lista ao inves no inicio, uma vez que 
        o raciocinio do lifo e fifo não tinha em conta que a eliminação do nó era no primeiro indice,
        corrigido no dia 22 de maio

        Args:
            no (No): nó que vai ser inserido
        """
        self._nos.insert(0, no)
