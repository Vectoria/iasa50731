from ecr.comportamento import Comportamento

class Explorar(Comportamento):
    """
    Classe que é um sub-comportamento, ou seja, esta a cumprir um sub-objetivos 

    Acoplamente alto por ser herança

    Args:
        Comportamento (Comportamento): extende
    """    
    def activar(percepcao):
        raise InterruptedError