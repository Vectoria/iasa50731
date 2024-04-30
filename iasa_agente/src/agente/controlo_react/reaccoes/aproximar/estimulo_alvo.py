from ecr.estimulo import Estimulo
from sae import Elemento


class EstimuloAlvo(Estimulo):
    """
    acoplamento alto por implementar
    contém fatorização

    A classe é a representação de um estimulo para encontrar algum alvo

    Args:
        Estimulo (Estimulo): implementa
    """

    def __init__(self, direcao, gama=0.9):
        """

        Args:
            direcao (Direcao): direção da sua visibilidade
            gama (float, optional): base da potencia de uma função exponencial decrescente. Defaults to float(0.9).
        """
        # programação de diferenca

        self.__direcao = direcao
        self.__gama = gama

    def detectar(self, percepcao):
        """
        Tenta detectar algum alvo, onde se houver, retorna a intensidade do estimulo com
        a multiplicação do gama com a distancia para tal alvo

        Args:
            percepcao (Percepcao): associação, para ter o alvo e distancia

        Returns:
            float: é a intensidade detectada pelo estimulo
        """
        elemento, distancia, _ = percepcao[self.__direcao]
        if elemento == Elemento.ALVO:
            return self.__gama ** distancia
        else:
            return 0
