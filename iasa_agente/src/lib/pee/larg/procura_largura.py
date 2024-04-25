from pee.mec_proc.fronteira_fifo import FronteiraFIFO
from .procura_grafo import ProcuraGrafo


class ProcuraLargura(ProcuraGrafo):
    """
    Possuí alto acoplamento por extender

    Pega tudo que o ProcuraGrafo e o MecanismoProcura faz, e apenas inicia a fronteira como FIFO,
    desta forma explora-se os nós mais antigos

    Possui uma exploração exaustiva de cada nível de procura, mas graças a ProcuraGrafo, diminui 
    a exasutão e aumenta a sua eficiencia, em termos de recursos

    Args:
        ProcuraGrafo (ProcuraGarfo): extende
    """

    def __init__(self):
        super().__init__(FronteiraFIFO)
