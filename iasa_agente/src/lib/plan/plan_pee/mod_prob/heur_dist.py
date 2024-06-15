from math import dist
from pee.melhor_prim.heuristica import Heuristica


class HeurDist(Heuristica):
    """
    A classe representa uma heuristica admissível de distancia euclidiana
    Erro da semana 10, onde estava mal escrito o nome do ficheiro,
    corrigido no dia 13 de junho

    Args:
        Heuristica (_type_): _description_
    """

    def __init__(self, estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        """
        a heuristica no caso, é a distancia da posição de um estado para o final
        Desta forma, ve-se qual é a menor distancia para o estado final, 
        onde usa-se a geometria euclidiana


        Args:
            estado (Estado): posicao atual

        Returns:
            double: retorna a distancia da posição atual ate ao objetivo 
        """
        return dist(estado.posicao, self.__estado_final.posicao)
