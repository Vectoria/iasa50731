from abc import ABC, abstractmethod


class Planeador(ABC):
    """
    interface a qual é a representação do raciocínio sobre meios (planeamento),
    em que gera planos e decide como pode ser feito as ações

    Args:
        ABC (ABC): interface
    """

    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """ define o plano """
        """
        Erro semana 10 que o método não tinha @abstractmethod, corrigido no dia 16 de junho, durante
        o desenvolvimento do relatorio
        """
