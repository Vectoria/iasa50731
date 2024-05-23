class MecUtil():
    """
    Classe que representa um mecanismo para expressões que tem a ver com utilidade de estado
    """

    def __init__(self, modelo, gama, delta_max):
        """
        O mecanismo de utilidade precisa do modelo das propriedades de Markov, de um gama e 
        delta max para definir o limite de iteração

        Args:
            modelo (ModeloPDM): obter o modelo das propriedades de Markov
            gama (double): multiplica com a utilidade
            delta_max (int): limite para iterar
        """
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    def utilidade(self):
        """
        Classe a qual conseguimos obter o dicionario da utilidade para cada
        estado possui a ação com maior valor do conjunto de ações neste estado

        Returns:
            Utilidade: Dicionario que tem estado associado a utilidade de ação
        """
        S, A = self.__modelo.S, self.__modelo.A
        u = dict()
        while (True):
            u_ant = u.copy()
            erro = 0
            for s in S():
                u.update(
                    {s: max(A(s), key=lambda a: self.util_accao(s, a, u_ant))}
                )
               # u[s]=  max(A(s), key=lambda a: self.util_accao(s, a, u_ant))
                erro = max((erro, abs(u[s]-u_ant[s])))
            if (erro > self.__delta_max):
                break
        return u

    def util_accao(self, s, a, U):
        """
        retorna o valor da ação dado a proximos estados, ou seja, terá em conta a transição e recompensa de 
        um estado para os proximos estados, juntamente com a utilidade do proximo estado (multiplicado por gama)

        Args:
            s (Estado): estado atual
            a (Operador): é a ação que esta a ser testada para ver o seu valor de utilidade
            U (Utilidade): usa o dicionario para encontrar o valor do proximo estado

        Returns:
            double: valor de utilidade de uma ação
        """
        valor = 0
        for s_linha in self.__modelo.S():
            valor += self.__modelo.T(s, a, s_linha) * \
                (self.__modelo.R(s, a, s_linha) + self.__gama * U[s_linha])
        return valor
