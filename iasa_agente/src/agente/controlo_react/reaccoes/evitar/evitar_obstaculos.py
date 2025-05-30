from .resposta_evitar import RespostaEvitar
from .evitar_dir import EvitarDir
from ecr.prioridade import Prioridade
from sae import Direccao


class EvitarObst(Prioridade):
    """
    Comportamento Composto que tem o mecanismo de prioridade dinamica

    Args:
        Prioridade (Prioridade): extend
    """

    def __init__(self):
        """
        Acontece uma fatorização, onde acontece uma list comprehension de maneira
        a criar varios comportamentos de EvitarDir, em todas as direções, onde o comportamento da direção
        que tiver mais prioridade, gerado pela sua resposta, será a que atuará no momento
        """
        self.__resposta = RespostaEvitar()
        super().__init__(
            [EvitarDir(direccao, resposta=self.__resposta) for direccao in Direccao])
