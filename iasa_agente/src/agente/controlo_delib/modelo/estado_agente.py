
from mod.estado import Estado


class EstadoAgente(Estado):
    """
    classe que representa a informação necessaria, tanto do modelo
    do mundo quanto para planeamento, onde a posição é o estado do agente

    Args:
        Estado (_type_): _description_
    """

    def __init__(self, posicao):
        self.__posicao = posicao

    def id_valor(self):
        return hash(self.__posicao)

    @property
    def posicao(self):
        return self.__posicao
