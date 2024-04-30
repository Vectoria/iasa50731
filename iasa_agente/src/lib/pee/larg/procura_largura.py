from ..mec_proc.fronteira_fifo import FronteiraFIFO
from .procura_grafo import ProcuraGrafo


class ProcuraLargura(ProcuraGrafo):
    """
    Possuí alto acoplamento por extender

    Pega tudo que o ProcuraGrafo e o MecanismoProcura faz (fatorização), e apenas inicia a fronteira como FIFO,
    desta forma explora-se os nós mais antigos

    Possui uma exploração exaustiva de cada nível de procura, mas graças a ProcuraGrafo, diminui 
    a exasutão e aumenta a sua eficiencia, em termos de recursos

    O seu critério de exploração é ser menor em profundidade

    Sua complexidade computacional temporal e espacial é calculada pelo
    factor de raminifação elevado a profundidade da procura, somando 1, onde é completo em encontrar a solução
    e ótimo em garantir que a a solução encontrada seja a que tenha menos custo

    Args:
        ProcuraGrafo (ProcuraGarfo): extende
    """

    def __init__(self):
        super().__init__(FronteiraFIFO)
