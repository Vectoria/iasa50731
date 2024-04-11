from ecr.reaccao import Reaccao
from ..resposta.resposta_mover import RespostaMover
from .estimulo_alvo import EstimuloAlvo


class AproximarDir(Reaccao):
    """
    Classe que representa uma reação (comportamento simples) para aproximar numa direção estimulada,
    em que é estimulado depedendo da distancia ao alvo

    Contém um acoplamento forte por ser extendido

    Args:
        Reaccao (Reaccao): Extende
    """

    def __init__(self, direcao):
        """
        dependedo da direção, detecta-se um estimulo, que gera a sua intensidade
        tal intensidade gerará uma prioridade ao movimento (resposta) a tal direção 

        Args:
            direcao (Direcao): A direção para onde olha
        """
        if direcao is not None:
            super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao))
