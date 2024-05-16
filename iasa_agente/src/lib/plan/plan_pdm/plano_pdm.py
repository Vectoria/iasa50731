from ..plano import Plano


class PlanoPDM(Plano):
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        raise InterruptedError

    def mostrar(self, vista):
        raise InterruptedError
