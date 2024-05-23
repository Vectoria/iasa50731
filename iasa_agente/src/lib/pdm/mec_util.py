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
        Classe a qual conseguimos obter o dicionario da utilidade final para cada
        estado possui a ação com maior valor do conjunto de ações neste estado, isso
        se o estado não for terminal que este não possui nenhuma ação em um estado,
        segue o pseudo-código do slide 21 do capitulo 15

        Iniciamos o dicionario a 0 em todos os estados e com o processo recursivo, 
        consegue-se ter o dicionario final da utilidade

        O delta é a diferença maxima de utilidade inicial com a seguinte

        Observa-se objetos de modelo, ao declarar as variaveis S e A, para depois invocar o método,
        a vantagem é que deixa o código mais legivel

        Por não ter do-while em python, usamos o while ate dar chegar a condição e dar um break

        Também, a nível de programação, existe o shadow copy do U_ant, de maneira não afetar o dicionario original

        Returns:
            Utilidade: Dicionario que tem estado associado a utilidade final de ação
        """
        S, A = self.__modelo.S, self.__modelo.A
        U = {s: 0.0 for s in S()}
        while True:
            U_ant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([self.util_accao(s, a, U_ant)
                           for a in A(s)], default=0
                           )
                delta = max(delta, abs(U[s]-U_ant[s]))
            if (delta <= self.__delta_max):
                break
        return U

    def util_accao(self, s, a, U):
        """
        retorna o valor da ação dado a proximos estados, ou seja, terá em conta a transição e recompensa de 
        um estado para os proximos estados, juntamente com a utilidade do proximo estado (multiplicado por gama)

        Notamos que usamos o método do python designado de sum, a qual substitui um ciclo for na qual acontece a soma

        Erro na semana 11, em que não tinha o estado seguinte bem, usava um ciclo for ao inves do método sum, corrigido
        na semana 12, dia 23 de maio

        Args:
            s (Estado): estado atual
            a (Operador): é a ação que esta a ser testada para ver o seu valor de utilidade
            U (Utilidade): usa o dicionario para encontrar o valor do proximo estado

        Returns:
            double: valor de utilidade de uma ação
        """
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        gama = self.__gama
        return sum(T(s, a, sn) * (R(s, a, sn) + gama * U[sn])
                   for sn in suc(s, a))
