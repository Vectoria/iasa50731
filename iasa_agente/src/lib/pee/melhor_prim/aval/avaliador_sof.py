from .avaliador_heur import AvaliadorHeur


class AvaliadorSof(AvaliadorHeur):
    """

    Args:
        AvaliadorHeur (AvaliadorHuer): classe ao qual faz a avaliação da procura sôfrega, no qual é h(n)
    """

    def prioridade(self, no):
        return self._heuristica.h(no.estado)
