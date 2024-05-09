from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof


class ProcuraSofrega(ProcuraInformada):
    """
    Classe que representa a procura sôfrega, onde tem a heuristica (conhece o dominio do problema), 
    h(n), onde acontece a minimização da estimativa de custo para atingir o objetivo, sendo sub-ótima solução
    e com menor complexidade computacional em comparação com a procura de custo uniforme, mas apresenta a desvantagem
    de que não tem em conta o custo do percurso já explorado

    Args:
        ProcuraInformada (ProcuraInformada): estende, por conhecer o dominio do problema
    """

    def __init__(self):
        """inicia-se super construtor com o avaliador sofrega
        """
        super().__init__(AvaliadorSof())
