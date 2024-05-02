from .avaliador import Avaliador


class AvaliadorHeur(Avaliador):
    def definir_heuristica(self, heuristica):
        """como o nome diz, define-se a heuristica

        Args:
            heuristica (_type_): _description_
        """
        self._heuristica = heuristica
