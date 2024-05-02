from .avaliador_heur import AvaliadorHeur


class AvaliadorAA(AvaliadorHeur):
    def prioridade(self, no):
        return super().prioridade(no)
