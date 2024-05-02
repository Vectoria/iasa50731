from .avaliador_heur import AvaliadorHeur


class AvaliadorSof(AvaliadorHeur):
    """classe ao qual faz a avaliação da procura sôfrega, no qual é h(n)

    Args:
        AvaliadorHeur (AvaliadorHuer): _description_
    """

    def prioridade(self, no):
        return self._heuristica.h(no.estado)
