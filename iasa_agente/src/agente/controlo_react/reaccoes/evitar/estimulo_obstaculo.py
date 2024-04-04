from ecr.estimulo import Estimulo
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento

class EstimuloObstaculo(Estimulo):
    """

    Args:
        Estimulo (Estimulo): _description_
    """    
    def __init__(self, direcao, intensidade=float(1)):
        self.__direcao=direcao
        self.__intensidade= intensidade

    def detectar(self,percepcao):
        elemento, distancia, _ = percepcao[self.__direcao]
        if percepcao.contacto_obst(self.__direcao):
            
            intensidade = self.__intensidade ** distancia
        else:
            intensidade= 0
        return intensidade