from pee.mec_proc.fronteira_fifo import FronteiraFIFO
from .procura_grafo import ProcuraGrafo


class ProcuraLargura(ProcuraGrafo):
    def __init__(self):
        super().__init__(FronteiraFIFO)
