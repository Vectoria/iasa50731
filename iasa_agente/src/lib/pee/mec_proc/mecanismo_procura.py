from abc import ABC, abstractmethod

from .no import No
from .solucao import Solucao


class MecanismoProcura(ABC):
    """
    É uma classe abstracta, possuí um acoplamento fraco por apenas ter associação e dependencias
    Classe que possibilida a exploração de possiveis opções de um problema, de maneira a encontrar
    uma solução por via de uma simulação prospectiva, atráves duma representação do dominio do problema

    Args:
        ABC (ABC): para tornar numa classe abstracta
    """

    def __init__(self, fronteira):
        """inicia a fronteira

        Args:
            fronteira (Fronteira): associação
        """
        self._fronteira = fronteira

    def _iniciar_memoria(self):
        """inicia-se a memoria do mecanismo, onde a lista começa vazia
        """
        self._fronteira.iniciar()

    @abstractmethod
    def _memorizar(self, no):
        """
        metodo abstracto
        tal método serve para memorizar os nós já explorados
        """

    def procurar(self, problema):
        """
        segue o slide 9 do capitulo pee, só que sem ter em conta a fronteira LIFO

        Tal metodo representa a procura de uma nó

        criamos um nó com o estado inicial do problema, de seguida memoriza-se,
        verifica se a fronteira não esteja vazia, durante este tempo, elimina-se do nó, a primeira fronteira
        seguidamente verificamos se o problema ja esta no objetivo, caso esteja, returnamos a solução,
        caso não, fazemos um ciclo em que expande a lista dos nós abertos e memoriza 


        Args:
            problema (Problema):  para criar um nó, percorrer as listas abertas
            ou para chegar ao nó com o objetivo

        Returns:
            Solucao: retorna a solução do problema, se encontrar
        """
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            if problema.objetivo(no.estado):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)

    def _expandir(self, problema, no):
        """
        segue o slide 10 do capitulo pee

        metodo que retira os nós e operatores, e mostra os nós sucessores


        Args:
            problema (_type_): _description_
            no (_type_): _description_

        Returns:
            list: _description_
        """
        sucessores = []
        estado = no.estado
        for operator in problema.operadores:
            estado_suc = operator.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operator.custo(estado, estado_suc)
                no_sucessor = No(estado_suc, operator, no, custo)
                sucessores.append(no_sucessor)
        return sucessores
