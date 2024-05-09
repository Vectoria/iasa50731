from math import dist
from .operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan
from sae import Direccao


class ModeloMundo(ModeloPlan):
    def __init__(self):
        self.__alterado = False
        raise NotImplementedError

    def obter_estado(self):
        return self.__estado

    def obter_estados(self):
        return self.__estados

    def obter_operadores(self):
        return self.__operadores

    def obter_elemento(self, estado):
        return self.__elementos.get(estado)

    def distancia(self, estado):
        dist(self.__estado, estado)

    def actualizar(self, percepcao):
        """
        Tendo em conta o que a percepção fornece, conseguimos obter
        o estado/s (posiç(ão)/(ões)), operadores (direccoes), e elementos,
        onde acontece uma alteração no modelo do mundo (quando recebe alguma percepção diferente)

        Args:
            percepcao (_type_): _description_
        """

        self.__estado = percepcao.posicao  # if self.__estado != percepcao.posicao
        self.__estados = percepcao.posicoes  # if self.__estados != percepcao.posicoes \
        # else self.__estados
        self.__operadores = [OperadorMover(
            self, direccao) for direccao in Direccao]
        self.__elementos = percepcao.elementos  # .get(self.__estado)
        self.__alterado = True  # if self.__alterado != True else \
        # self.__alterado #talvez seja errado

    def mostrar(self, vista):
        raise NotImplementedError

    @property
    def alternado(self):
        return self.__alterado
