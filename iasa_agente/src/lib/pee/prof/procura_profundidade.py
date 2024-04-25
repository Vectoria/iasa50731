
from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.fronteira_lifo import FronteiraLIFO


class ProcuraProfundidade(MecanismoProcura):
    """_summary_

    Args:
        MecanismoProcura (MecanismoProcura): _description_
    """

    def __init__(self):
        super().__init__(FronteiraLIFO())

    def _memorizar(self, no):
        self._fronteira.inserir(no)
