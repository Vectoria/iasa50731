from .procura_melhor_prim import ProcuraMelhorPrim


class ProcuraInformada(ProcuraMelhorPrim):
    def procurar(self, problema, heuristica):
        return super().procurar(problema)
