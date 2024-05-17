
from pee.melhor_prim.procura_aa import ProcuraAA
from .plano_pee import PlanoPEE
from .mod_prob.huer_dist import HeurDist
from .mod_prob.problema_plan import ProblemaPlan
from ..planeador import Planeador


class PlaneadorPEE(Planeador):
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
            # print(estado_final.posicao)
            problema = ProblemaPlan(modelo_plan, estado_final)
            # print(problema.estado_inicial.posicao)
            heuristica_dist = HeurDist(estado_final)
            # print(heuristica_dist.h(problema.estado_inicial))
            solucao = self.__mec_pee.procurar(problema, heuristica_dist)
            if solucao:
                return PlanoPEE(solucao)
