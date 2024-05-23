from ..plan_pee.mod_prob.huer_dist import HeurDist
from ..plan_pee.mod_prob.problema_plan import ProblemaPlan
from ..modelo.modelo_plan import ModeloPlan
from ..planeador import Planeador


class PlaneadorPDM(Planeador):
    """
    Classe que representa o raciocínio sobre meios das propriedas de Markov

    Args:
        Planeador (Planeador): raciocinio sobre meios
    """

    def __init__(self, gama=0.85, delta_max=1):
        self.__gama = gama
        self.__delta_max = delta_max
        # self.__modelo_plan = ModeloPlan()

    def planear(self, modelo_plan, objetivos):
        """ if objetivos:
            estado_final = objetivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica_dist = HeurDist(estado_final) """
        raise InterruptedError
