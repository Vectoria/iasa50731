from ..plano import Plano


class PlanoPEE(Plano):
    """
    Classe que representa o plano da procura de espaço em estados

    Args:
        Plano (Plano): implementa a interface
    """

    def __init__(self, solucao):
        self.__solucao = solucao
        self.__passos = [passo for passo in self.__solucao]

    def obter_accao(self, estado):
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operador

    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao,
                                     passo.operador.ang)
