
from mec_proc.mecanismo_procura import MecanismoProcura
from mec_proc.fronteira_lifo import FronteiraLIFO


class ProcuraProfundidade(MecanismoProcura):
    def __init__(self):
        super().__init__(FronteiraLIFO())

    def _memorizar(self, no):
        return super()._memorizar(no)
