
from mod.problema import Problema


class ProblemaPlan(Problema):
    """
    classe que representa o dominio do problema do plano

    Args:
        Problema (_type_): _description_
    """

    def __init__(self, modelo_plan, estado_final):
        # self.__modelo_plan = modelo_plan
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    def objetivo(self, estado):
        return estado == self.__estado_final
