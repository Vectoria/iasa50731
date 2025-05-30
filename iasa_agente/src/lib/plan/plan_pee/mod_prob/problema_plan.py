
from mod.problema import Problema


class ProblemaPlan(Problema):
    """
    classe que representa o dominio do problema do mundo

    Args:
        Problema (Problema): estende da classe abstrata, ganhando forma para o problema do mundo
    """

    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    def objetivo(self, estado):
        return estado == self.__estado_final
