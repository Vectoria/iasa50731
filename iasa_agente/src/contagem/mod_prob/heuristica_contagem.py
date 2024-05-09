from pee.melhor_prim.heuristica import Heuristica
from .estado_contagem import EstadoContagem


class HeuristicaContagem(Heuristica):
    def __init__(self, estado_final):
        """
        inicia o valor do estado final

        Args:
            estado_final (_type_): _description_
        """
        self._estado_final = estado_final

    def h(self, estado):
        """
        É a diferença do valor do estado final com o valor do estado

        Args:
            estado (Estado): Usa-se o valor do estado atual

        Returns:
            Double: retorna a diferença
        """
        return self._estado_final - estado.valor
