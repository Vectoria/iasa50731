class MecUtil():
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    def utilidade(self):
        S, A = self.__modelo.S, self.__modelo.A
        u = dict()
        while (True):
            u_ant = u.copy()
            erro = 0
            for s in S():
                u.update(s=max(A(s), key=lambda a: self.util_accao(s, a, u_ant)))
                erro = max((erro, abs(u[s]-u_ant[s])))
            if (erro > self.__delta_max):
                break
        return u

    def util_accao(self, s, a, U):
        for s_linha in self.__modelo.S():
            self.__modelo.T(s, a, s_linha)
        raise InterruptedError
