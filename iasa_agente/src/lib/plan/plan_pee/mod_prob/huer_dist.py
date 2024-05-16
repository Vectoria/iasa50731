from math import dist
from pee.melhor_prim.heuristica import Heuristica


class HeurDist(Heuristica):
    def __init__(self, estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        """
        a heuristica no caso, é a distancia da posição de um estado para o final
        Desta forma, ve-se qual é a menor distancia para o estado final, 
        onde usa-se a geometria euclidiana


        Args:
            estado (_type_): _description_

        Returns:
            _type_: _description_
        """
        return dist(estado, self.__estado_final)
