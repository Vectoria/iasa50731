from ecr.estimulo import Estimulo
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento

class EstimuloAlvo(Estimulo):
    def __init__(self, direcao, gama=float(0.9)): #por float?
        """_summary_

        Args:
            direcao (_type_): _description_
            gama (_type_, optional): base da potencia de uma função exponencial decrescente. Defaults to float(0.9).
        """        
        #programação de diferenca
        
        self.__direcao=direcao
        self.__gama= gama
        ""

    def detectar(self,percepcao):
        #self.direccao= percepcao.direccao
        elemento, distancia, _ = percepcao[self.__direcao]
        if elemento == Elemento.ALVO:
            intensidade = self.__gama ** distancia
        else:
            intensidade= 0
        return intensidade
    