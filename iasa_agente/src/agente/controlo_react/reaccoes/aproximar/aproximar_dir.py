from ecr.reaccao import Reaccao

class AproximarDir(Reaccao):
    """
    Classe que representa uma reação (comportamento simples) para aproximar numa direção estimulada,
    em que é estimulado depedendo da distancia ao alvo

    Contém um acoplamento forte por ser extendido

    Args:
        Reaccao (Reaccao): Extende
    """    
    def __init__(self, direcao):
        #raise InterruptedError
        ""