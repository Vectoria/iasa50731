from abc import ABC, abstractmethod


class Heuristica(ABC):
    """
    interface que representa a heurística
    onde acontece uma estimativa de custo do percurso, refletindo
    o conhecimento sobre o domínio do problema para guiar a procura

    Args:
        ABC (ABC): interface
    """
    @abstractmethod
    def h(self, estado):
        """ 
        define, nas implementações desta
        a heurística para estimar
        """
