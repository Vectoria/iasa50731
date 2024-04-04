from ecr.reaccao import Reaccao
from ..resposta.resposta_mover import RespostaMover
from .estimulo_obstaculo import EstimuloObstaculo


class EvitarDir(Reaccao):
    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObstaculo(direccao), resposta(direccao))
