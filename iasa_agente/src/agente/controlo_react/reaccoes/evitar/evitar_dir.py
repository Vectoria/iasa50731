from ecr.reaccao import Reaccao
from .estimulo_obstaculo import EstimuloObstaculo


class EvitarDir(Reaccao):
    """
    É um comportamento com mémoria

    Representa a reação para evitar uma direção caso tenha obstaculo

    Args:
        Reaccao (Reaccao): extend, por ser um comportamento
    """

    def __init__(self, direccao, resposta):
        """
        Verifica o estimulo com a direção que está, gera uma intensidade,
        tal intensidade gerará uma prioridade ao movimento (resposta) a tal direção 

        Args:
            direccao (Direccao): associação
            resposta (Resposta): associação
        """
        super().__init__(EstimuloObstaculo(direccao), resposta)
