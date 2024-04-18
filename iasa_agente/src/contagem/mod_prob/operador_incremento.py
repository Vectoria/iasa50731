from .estado_contagem import EstadoContagem
from mod.operador import Operador


class OperadorIncremento(Operador):

    def __init__(self, incremento):
        self.__incremento = incremento

    def aplicar(self, estado):
        """é uma ação, onde acontece uma transição de estado

        Tal transição faz como que o novo estado incremento o seu valor atual

        Args:
            estado (Estado): usamos o valor atual do estado

        Returns:
            Estado: retorna um estado onde tem o seu valor + o incremento
        """
        return EstadoContagem(estado.valor + self.__incremento)

    def custo(self, estado, estado_suc):
        return estado.valor > estado_suc.valor
