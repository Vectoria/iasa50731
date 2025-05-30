
from pee.melhor_prim.procura_aa import ProcuraAA
from .plano_pee import PlanoPEE
from .mod_prob.heur_dist import HeurDist
from .mod_prob.problema_plan import ProblemaPlan
from ..planeador import Planeador


class PlaneadorPEE(Planeador):
    """
    classe que representa o planeador de procura em espaço de estados

    Args:
        Planeador (Planeador): implementa a interface
    """

    def __init__(self):
        # podia ser outras procuras que sejam informadas
        self.__mec_pee = ProcuraAA()

    def planear(self, modelo_plan, objetivos):
        """ 
        instanciar o problema e heuristica, de maneira que aconteça a procura
        pelo mecanismo, e caso encontra a solução, retorna o PlanoPEE passando a solução

        Erro na semana 10, onde faltava a verificação se tinha objetivos para começar a planear 
        """
        if objetivos:
            estado_final = objetivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica_dist = HeurDist(estado_final)
            solucao = self.__mec_pee.procurar(problema, heuristica_dist)
            if solucao:
                return PlanoPEE(solucao)
