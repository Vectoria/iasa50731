from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA


class ProcuraAA(ProcuraInformada):
    """
    Classe que representa a procura A*, um mix da procura custo uniforme e sôfrega, onde tem em conta
    a minimização do custo acumulado de cada nó explorado, minimiza a estimativa de custo
    para antingir o objetivo, onde apresenta uma solução otima, com pouca complexidade computacional

    A heurística admissível para as distancias Euclidianas e de Manhattan (se não for possivel moviemntos diagonais),
    em que o custo estimado é inferior ou igual ao custo mínimo

    Args:
        ProcuraInformada (ProcuraInformada): estende
    """

    def __init__(self):
        """inicia-se o contrutor com a super classe com o avaliador do tipo a*
        """
        super().__init__(AvaliadorAA())
