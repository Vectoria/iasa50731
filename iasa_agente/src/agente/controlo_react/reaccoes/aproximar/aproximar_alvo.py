from ecr.prioridade import Prioridade
from .aproximar_dir import AproximarDir
from sae.ambiente.direccao import Direccao

class AproximarAlvo(Prioridade):
    """
    Esta classe é representação de um comportamento com prioridade dinamica,
    em que temos uma lista de comportamentos simples (reações), todos estes são comportamentos estmulos para aproximar numa das 
    direções (norte, sul, este e oeste), respeita o diagrama informal do slide 11

    Contém um acoplamento forte por ser extend


    Args:
        Prioridade (Prioridade): extende
    """    
    __comportamentos=[AproximarDir(Direccao.NORTE),AproximarDir(Direccao.SUL),AproximarDir(Direccao.ESTE),AproximarDir(Direccao.OESTE)]
    def __init__(self):
        """
        factorização, , usa a classe dos comportamentos compostos para ser incializado,
        introduzindo os comportamentos
        """        
        super().__init__(self.__comportamentos)
        