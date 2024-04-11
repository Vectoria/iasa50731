from abc import ABC, abstractclassmethod


class Fronteira(ABC):
    def __init__(self):
        self.iniciar()

    def iniciar(self):
        self.nos = []

    @abstractclassmethod
    def inserir(self, no):
        """  """

    def remover(self):
        """_summary_

        Returns:
            list: retorna a lista sem o primeiro elemento
        """
        return self.nos.pop(0)

    @property
    def vazia(self):
        return len(self.nos) == 0
