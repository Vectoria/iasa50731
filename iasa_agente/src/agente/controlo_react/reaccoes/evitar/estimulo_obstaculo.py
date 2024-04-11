from ecr.estimulo import Estimulo
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento


class EstimuloObstaculo(Estimulo):
    """
    alto acoplamento por implementar uma interface
    contém fatorização estrutural ??????????????????????????????????

    A classe é a representação de um estimulo de encontrar obstaculos

    Args:
        Estimulo (Estimulo): implementa
    """

    def __init__(self, direcao, intensidade=float(1)):
        """
        Inicia a direção atual, com uma intensidade a 1 de momento

        Args:
            direcao (Direcao): associação
            intensidade (float, optional): Defaults to float(1).
        """
        self.__direcao = direcao
        self.__intensidade = intensidade

    def detectar(self, percepcao):
        """
        Atualiza a intensidade a partir da percepção da direçao atual, caso
        a percepção detecta algum obstaculo, atualiza a intensidade com a multiplicação
        da intensidade atual com a distancia a tal obstaculo, caso não aconteça a 
        condição, retorna a intensidade a nulo

        Args:
            percepcao (Percepcao): para ter a distancia e ver se esta em contacto com algum obstaculo

        Returns:
            float: a intensidade causada pelo estimulo
        """
        elemento, distancia, _ = percepcao[self.__direcao]
        if percepcao.contacto_obst(self.__direcao):

            intensidade = self.__intensidade ** distancia
        else:
            intensidade = 0
        return intensidade
