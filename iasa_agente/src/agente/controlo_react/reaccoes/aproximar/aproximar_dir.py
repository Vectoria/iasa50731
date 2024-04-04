from ecr.reaccao import Reaccao
from ..resposta.resposta_mover import RespostaMover
from .estimulo_alvo import EstimuloAlvo

class AproximarDir(Reaccao):
    """
    Classe que representa uma reação (comportamento simples) para aproximar numa direção estimulada,
    em que é estimulado depedendo da distancia ao alvo

    Contém um acoplamento forte por ser extendido

    Args:
        Reaccao (Reaccao): Extende
    """    
    def __init__(self, direcao):
        #super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao))
        """self.direcao= direcao
        
        if direcao is not None:
            self.__resposta= RespostaMover(self.direcao)
            self.__estimulo= EstimuloAlvo(self.direcao) 
            """
        #super().__init__(self.__estimulo,self.__resposta)
        if direcao is not None:
            super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao)) 
        ""