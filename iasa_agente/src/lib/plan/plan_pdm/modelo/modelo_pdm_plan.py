from agente.controlo_delib.modelo.operador_mover import OperadorMover  # TODO
from pdm.modelo.modelo_pdm import ModeloPDM


class ModeloPDMPlan(ModeloPDM):
    """
    Classe que representa o modelo plano das propriedade de Markov definido

    Args:
        ModeloPDM (ModeloPDM): implementa a interface
    """

    def __init__(self, modelo_plan, objetivos, rmax=1000):
        self.__modelo_plan = modelo_plan
        self.__objetivos = objetivos
        self.__rmax = rmax

    def obter_estado(self):
        return self.__objetivos[0]

    def obter_estados(self):
        return self.__objetivos

    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    def S(self):
        return self.__objetivos

    def A(self, s):
        # return OperadorMover(s)
        raise InterruptedError

    def T(self, s, a, sn):
        raise InterruptedError

    def R(self, s, a, sn):
        raise InterruptedError

    def suc(self, s, a):
        raise InterruptedError
