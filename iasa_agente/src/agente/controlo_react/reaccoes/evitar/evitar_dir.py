from ecr.reaccao import Reaccao
from ..resposta.resposta_mover import RespostaMover
from .estimulo_obstaculo import EstimuloObstaculo


class EvitarDir(Reaccao):
    """
    É um comportamento com mémoria

    Args:
        Reaccao (Reaccao): extend, por ser um comportamento
    """

    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObstaculo(direccao), resposta)
