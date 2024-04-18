from pee.prof.procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    def procurar(self, problema, inc_prof=1, limite_prof=100):
        """
        implementa o pseudo-codigo do slide 11 do capitulo 11

        polimorfismo por ativar o metodo usado a super classe, de maneira que encontramos a 
        solução

        Args:
            problema (_type_): _description_
            inc_prof (int, optional): incrementação da profundidade. Defaults to 1.
            limite_prof (int, optional): _description_. Defaults to 100.

        Returns:
            None | Solução: Se não for encontrado a solução, retorna none, se sim
            retorna a solução 
        """
        for profundidade in range(0, limite_prof+1, inc_prof):
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao
