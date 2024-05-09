from .procura_melhor_prim import ProcuraMelhorPrim


class ProcuraInformada(ProcuraMelhorPrim):
    """
    Classe ao qual redifine apenas o método procurar, dinamicamente

    É uma classe abstacta, a qual aproveita o conhecimento do domínio do problema
    em que acontece uma exploração seletiva do espaço de estados por ter uma
    procura guiada

    Esta procura tem a noção da heurística (h(n))

    As procuras que origina desta classe, são a sôfraga e a A*

    Args:
        ProcuraMelhorPrim (ProcuraMelhorPrim): extend
    """

    def procurar(self, problema, heuristica):
        """
        acontece uma redifinição desta classe
        heuristica serve para configurar o avaliador, dando a noção de estimativa,
        seguidamente fazemos o super do método (fatorização estrutural)

        Args:
            problema (Problema): para procurar o problema
            heuristica (Heuristica): estimativa

        """
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
