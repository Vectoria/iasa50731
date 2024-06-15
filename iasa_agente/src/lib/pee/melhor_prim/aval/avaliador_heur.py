from .avaliador import Avaliador


class AvaliadorHeur(Avaliador):
    def definir_heuristica(self, heuristica):
        """
        Args:
            heuristica (Heuristica): como o nome diz, define-se a heuristica
        """
        self._heuristica = heuristica
