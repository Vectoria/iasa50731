from .passo_solucao import PassoSolucao


class Solucao:
    def __init__(self, no_final):
        """


        Args:
            no_final (_type_): _description_
        """
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo)
            no = no.antecessor

    @property
    def dimensao(self):
        """profundidade da solução
        """
        return self.__no_final.profundidade

    @property
    def custo(self):
        """retorna o custo total da solução
        """
        return self.__no_final.custo

    def __iter__(self):
        return iter(self.__passos)

    def __getitem__(self, index):
        return self.__passos[index]
