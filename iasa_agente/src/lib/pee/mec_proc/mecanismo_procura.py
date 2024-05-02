from abc import ABC, abstractmethod

from .no import No
from .solucao import Solucao


class MecanismoProcura(ABC):
    """
    É uma classe abstracta, possuí um acoplamento fraco por apenas ter associação e dependencias
    Classe que possibilida a exploração de possiveis opções de um problema, de maneira a encontrar
    uma solução por via de uma simulação prospectiva, atráves duma representação do dominio do problema

    Esta classe já apresenta de uma maneira um pouco concreta, o espaço de estados

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

        O proposito para o qual verifica-se se a fronteira não esteja vazia, é pelo o facto de que se ela fosse 
        vazia, isso indicaria que não haveria soluções do problema


        Args:
            problema (Problema):  para criar um nó, percorrer as listas abertas
            ou para chegar ao nó com o objetivo

        Returns:
            Solucao: retorna a solução do problema, se encontrar
        """
        self._iniciar_memoria()
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

        Metodo que mostra os nós sucessores, ou seja, expande de um nó aberto

        Inicializamos uma lista para os nós sucessores, percorremos os operadores, em que cada operador
        gera um estado sucessor do nó aberto, de seguida calculasse o custo do nó antecessor juntamento com o custo 
        da transição para o estado sucessor, gera um nó sucessor e adiciona o mesmo a lista, por fim de percorrer
        os operadores existentes, retorna a lista de nós

        Args:
            problema (Problema): serve para usar todos os operadores
            no (No): Nó aberto que será expandido

        Returns:
            list: retorna uma lista de estados sucessores
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
