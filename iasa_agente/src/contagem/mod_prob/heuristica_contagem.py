from pee.melhor_prim.heuristica import Heuristica


class HeuristicaContagem(Heuristica):
    def __init__(self, estado_final):
        """
        inicia o valor do estado final
        """
        self._estado_final = estado_final

    def h(self, estado):
        """
        É a diferença do valor do estado final com o valor do estado

        Erro na semana 9, onde não tinha o abs de valor absoluto

        Args:
            estado (Estado): Usa-se o valor do estado atual

        Returns:
            Double: retorna a diferença
        """
        return abs(self._estado_final - estado.valor)
