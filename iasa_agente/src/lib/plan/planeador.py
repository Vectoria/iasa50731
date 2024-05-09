from abc import ABC, abstractmethod


class Planeador(ABC):
    def planear(self, modelo_plan, objetivos):
        """ define o plano """
