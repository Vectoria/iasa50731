from .procura_melhor_prim import ProcuraMelhorPrim
from .aval.avaliador_custo_unif import AvaliadorCustoUnif


class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
    É a representação da procura de custo uniforme (f(n)=g(n)), onde apresenta
    otima solução mas contém um nível de complexidade computacional gigantesco,
    consiste na minimização do custo acumulado de cada nó explorado (feito pelo avaliador desta
    classe)

    Este é uma procura que não é informada, por não aproveitar o conhecimento do domínio do 
    problema, onde a exploração é exaustiva por explorar o espaço de estados, por não existir
    a uma procura guiada

    Args:
        ProcuraMelhorPrim (ProcuraMelhorPrim): estende
    """

    def __init__(self):
        super().__init__(AvaliadorCustoUnif())
