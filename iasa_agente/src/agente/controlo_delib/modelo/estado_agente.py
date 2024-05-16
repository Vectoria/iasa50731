
from mod.estado import Estado


class EstadoAgente(Estado):
    """
    Classe que representa a informação necessaria, tanto do modelo
    do mundo quanto para planeamento, onde a posição é o estado do agente no mundo

    Possui forte coesão e acoplamento médio a fraco, por estender de uma classe abstracta (principio
    de arquitetura de software, abstração)

    Args:
        Estado (Estado): estende
    """

    def __init__(self, posicao):
        self.__posicao = posicao

    def id_valor(self):
        return hash(self.__posicao)

    @property
    def posicao(self):
        return self.__posicao
