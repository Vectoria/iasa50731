from ..modelo.modelo_plan import ModeloPlan
from ..planeador import Planeador


class PlaneadorPDM(Planeador):
    def __init__(self, gama=0.85, delta_max=1):
        self.__gama = gama
        self.__delta_max = delta_max
        self.__modelo_plan = ModeloPlan()

    def planear(self, modelo_plan, objetivos):
        raise InterruptedError
