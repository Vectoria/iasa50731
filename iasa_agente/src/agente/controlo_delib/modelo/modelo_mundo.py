from math import dist

from sae import Elemento, Direccao
from .estado_agente import EstadoAgente
from .operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan


class ModeloMundo(ModeloPlan):
    """
    Classe que representa um modelo do mundo, representação interna do ambiente, onde pode ter estado(s),
    operadores, elemento(s) e distancia entre posições, onde o mundo é dinamico, em que com o tempo pode existir
    aleterações dentro do modelo do mundo

    Args:
        ModeloPlan (ModeloPlan): implementa a interface
    """

    def __init__(self):
        self.__operadores = [OperadorMover(
            self, direccao) for direccao in Direccao]
        self.__recolha = False

    def obter_estado(self):
        return self.__estado

    def obter_estados(self):
        return self.__estados

    def obter_operadores(self):
        return self.__operadores

    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao)

    def distancia(self, estado):
        return dist(estado.posicao, self.__estado.posicao)

    def actualizar(self, percepcao):
        """
        Tendo em conta o que a percepção fornece, conseguimos obter
        o estado/s (posiç(ão)/(ões)), e elementos, além de quando o agente recolhe um alvo
        onde acontece uma recolha, ou seja, o mundo é alterado

        Correção no dia 16 de maio, onde a declaração não tinha em conta em instanciar
        a classe EstadoAgente; antes tinha um conjunto de operadores, mas por ser fixo foi para
        o construtor da classe; eliminou-se a afetação do altera e pos a recolha, que antes não existia

        Args:
            percepcao (Percepcao): para conseguir as informações exteriores ao agente
        """

        self.__estado = EstadoAgente(percepcao.posicao)
        self.__estados = [EstadoAgente(posicao)
                          for posicao in percepcao.posicoes]
        self.__elementos = percepcao.elementos
        self.__recolha = percepcao.recolha

    def mostrar(self, vista):
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
            vista.marcar_posicao(self.__estado.posicao)

    @property
    def alterado(self):
        """
        Erro da semana 10, sobre nomenclatura, onde ao ínves de estar escrito alterado, estava escrito alternado,
        corrigido no dia 16 de abril
        Returns:
            bool: quando houver recolha, sabe-se que houve alteração no mundo
        """
        return self.__recolha
