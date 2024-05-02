from abc import ABC, abstractmethod


class Avaliador(ABC):

    @abstractmethod
    def prioridade(self, no):
        """
        faz a prioridade através dos criterios feitos pelas classes
        que implementarão este metodo (sofre de polimorfismo)

        Args:
            no (No): atrela o valor da prioridade ao nó
        """
