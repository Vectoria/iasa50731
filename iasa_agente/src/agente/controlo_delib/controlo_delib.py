from .mec_delib import MecDelib
from modelo.modelo_mundo import ModeloMundo
from sae import Controlo


class ControloDelib(Controlo):
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__objetivos = []
        self.__modelo_mundo = ModeloMundo()
        self.__plano = None
        self.__controlo = MecDelib(self.__modelo_mundo_)
        # super().__init__()

    def processar(self, percepcao):
        self.assimilar(percepcao)
        if (self.reconsiderar()):
            self.deliberar()
            self.planear()
        return self.executar()

    def assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)

    def reconsiderar(self):
        return not self.__plano or self.__modelo_mundo.__alterado

    def deliberar(self):
        self.__objetivos = self.__controlo.deliberar()

    def planear(self):
        self.__plano = self.__planeador.planear(
            self.__modelo_mundo, self.__objetivos)

    def executar(self):
        if self.__plano:
            operador = self.__plano.obter_accao(
                self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao

    def mostrar(self):
        raise NotImplementedError
