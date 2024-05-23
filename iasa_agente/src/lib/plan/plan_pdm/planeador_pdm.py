from pdm.pdm import PDM
from plan.plan_pdm.plano_pdm import PlanoPDM
from ..plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from ..planeador import Planeador


class PlaneadorPDM(Planeador):
    """
    Classe que representa o raciocínio sobre meios das propriedas de Markov

    Implementa a interface a ainda assim modifica o menor codigo possivel, de maneira que seja funcional

    Args:
        Planeador (Planeador): raciocinio sobre meios
    """

    def __init__(self, gama=0.85, delta_max=1):
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objetivos):
        """

        Se existirem os objetivos, inicia-se o modelo plano das propriedades de Markov (associação 
        estrutural, uma fatorização no caso), com este modelo da para criar as propriedade de Markov,
        a qual devolve um dicionario de utilidades e politica, estes que são necessarios para
        instanciar o PlanoPDM, retornando o plano

        Args:
            modelo_plan (_type_): _description_
            objetivos (_type_): _description_

        Returns:
            _type_: _description_
        """
        if objetivos:
            modelo_pdm = ModeloPDMPlan(modelo_plan, objetivos)
            pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
            utilidade, pol = pdm.resolver()
            return PlanoPDM(utilidade, pol)
