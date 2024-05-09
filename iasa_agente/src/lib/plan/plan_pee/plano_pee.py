from ..plano import Plano


class PlanoPEE(Plano):
    def __init__(self, solucao):
        self.__solucao = solucao

    def obter_accao(self, estado):
       # if(self.__passos := [passo for passo in self.__solucao]):
        self.__passos = [passo for passo in self.__solucao]
        if (self.__passos):
            passo = self.__passos.pop(0)
            if passo == estado:
                return self.__passo.operador

    def mostrar(self, vista):
        raise NotImplementedError
