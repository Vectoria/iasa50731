from .procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    """
    Contém um alto acoplamento por extender

    A classe representa uma profundidade iterativa (em termos de de realizar uma procura em todos os limites
    da fronteira de um ilimite de profundidade crescente), com limites de profundidade crescentes,
    também baseia-se na procura de profundidade limitada, por ter um limite maximo

    Possuí fatorização por basear na procura de profundidade limite


    Args:
        ProcuraProfLim (ProcuraProfLim): extende
    """

    def procurar(self, problema, inc_prof=1, limite_prof=100):
        """
        implementa o pseudo-codigo do slide 11 do capitulo 11

        polimorfismo por ativar o metodo usado a super classe, de maneira que encontramos a 
        solução

        Realiza uma procura em profundidade com um limite de profundidade actual, tal limite é incrementado até um 
        certo ponto, no caso, quando chegar ao valor do limite_prof

        Args:
            problema (Problema): faz o super, ou seja, da os operadores
            inc_prof (int, optional): incrementação da profundidade por iteração. Defaults to 1.
            limite_prof (int, optional): a profundidade limitada. Defaults to 100.

        Returns:
            None | Solução: Se não for encontrado a solução, retorna none, se sim
            retorna a solução 
        """
        for profundidade in range(0, limite_prof+1, inc_prof):
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao
