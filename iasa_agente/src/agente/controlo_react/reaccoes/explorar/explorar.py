from ecr.comportamento import Comportamento
from ..resposta.resposta_mover_aleat import RespostaMoverAleat

class Explorar(Comportamento):
    """
    Classe que é um sub-comportamento, ou seja, esta a cumprir um sub-objetivos 
    Por ser um sub-comportamento, pode ser também um comportamento fixo (que só tem resposta)

    Acoplamente alto por ser herança

    Args:
        Comportamento (Comportamento): extende
    """    
    def activar(self,percepcao):
        """


        Args:
            percepcao (Percepcao): 

        Returns:
            Accao: retorna uma ação com movimento aleatorio mas com percepção
        """        
        resposta= RespostaMoverAleat()
        return resposta.activar(percepcao)