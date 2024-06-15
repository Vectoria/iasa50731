class No:
    """
    Possui fraco acoplamento por apenas ter associações

    Classe qeu representa o nó duma arvore de procura (conceitualmente é o espaço de estados), em que nela
    esta associado um estado, e opcionalmente, operador, antecessor e o custo.

    Opcional uma vez que se o nó for o inicial de uma arvore, não haveria operador, antecessor e custo deste
    """

    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        """ são 2 construtores, um que aceita so estado  
        e o outro que tem o estado, operdor, antecessor e custo (para isso, existe um default noutros parametros)

        Caso haja antecessor, incrementamos a profundidade (o nome da tatica é busca em profundidade)

        Args:
            estado (Estado): estado associado ao nó
            operador (Operador, optional): operador usado do antecessor para o nó atual. Defaults to None.
            antecessor (No, optional): nó anterior. Defaults to None.
            custo (int, optional): custo do nó. Defaults to 0.
        """
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo

        if antecessor:

            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def custo(self):
        return self.__custo

    @property
    def estado(self):
        return self.__estado

    @property
    def operador(self):
        return self.__operador

    @property
    def antecessor(self):
        return self.__antecessor

    def __lt__(self, other):
        """
        verifica se o custo do nó atual é menor que o outro

        Erro na semana 9, onde houve uma correção mal feita da minha parte sobre este código em que inverti 
        o sinal de menor para maior. Inicialmente, na semana 7 estava o sinal menor. Corrigido no dia 15 de junho

        Args:
            other (No): outro nó para comparar

        Returns:
            bool: 
        """
        return self.custo < other.custo
