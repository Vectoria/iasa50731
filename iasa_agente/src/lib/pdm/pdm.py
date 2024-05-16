from .mec_util import MecUtil


class PDM():
    def __init__(self, modelo, gama, delta_max):
        """
        acontece a associação estrutural com o MecUtil

        Args:
            modelo (_type_): _description_
            gama (_type_): _description_
            delta_max (_type_): _description_
        """
        self.__mec_util = MecUtil(modelo, gama, delta_max)
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    def politica(self, U):
        S, A = self.__modelo.S, self.__modelo.A
        pol = {}
        for s in S():
            if A(s):
                pol[s] = max(
                    A(s), key=lambda a: self.__mec_util.util_accao(s, a, U))
        return pol

    def resolver(self):
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U, pol
