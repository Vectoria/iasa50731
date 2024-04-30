
from ..mec_proc.mecanismo_procura import MecanismoProcura
from ..mec_proc.fronteira_lifo import FronteiraLIFO


class ProcuraProfundidade(MecanismoProcura):
    """
    Possui forte acoplamento por extender

    É um mecanismo de procura não informada, uma vez que não usa o domínio do problema para guiar a procura

    A fronteira será do tipo LIFO, porque primeiro explora os nós mais recentes, aumentando a profundidade
    de um ramo corrente

    A sua complexidade computacional é calculada pelo factor de ramificação a multiplicar com a profundidade da árvore, isso no termo espacial,
    já no termos temporal, é o factor de ramificação elevado a profundidade da árvore da procura
    Com isso, não é completo em mostrar a solução (não garante tal), e não é otimo (a solução encontrada pode ser a que tenha mais custo)

    Args:
        MecanismoProcura (MecanismoProcura): extende
    """

    def __init__(self):
        super().__init__(FronteiraLIFO())

    def _memorizar(self, no):
        """
        Args:
            no (No): adciona o nó no fim da lista de nós
        """
        self._fronteira.inserir(no)
