from .evitar_dir import EvitarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao
class EvitarObst(Prioridade):
    __comportamentos=[EvitarDir(Direccao.NORTE),EvitarDir(Direccao.SUL),EvitarDir(Direccao.ESTE),EvitarDir(Direccao.OESTE)]
    def __init__(self):
        """
        factorização, , usa a classe dos comportamentos compostos para ser incializado,
        introduzindo os comportamentos
        """        
        super().__init__(self.__comportamentos)
    
    ""