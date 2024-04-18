from abc import ABC, abstractmethod


class Fronteira(ABC):
    """
    Classe que representa a Fronteira, estrutura de dados com relação de ordem, em que
    determina estratégia de controlo da procura

    Args:
        ABC (ABC): para a classe ser abstracta
    """

    def __init__(self):
        """esvazia os nós
        """
        self.iniciar()

    def iniciar(self):
        """inicia uma lista vazia de nós, que mais tarde recebera outros nós nas classes que extendem desta classe
        """
        self.nos = []

    @abstractmethod
    def inserir(self, no):
        """ metodo abstracto """

    def remover(self):
        """
        remove o primeiro item, por ser fronteira de exploração, onde o primeiro item sempre sai

        Returns:
            list: retorna a lista sem o primeiro elemento
        """
        return self.nos.pop(0)

    @property
    def vazia(self):
        """verifica se a lista esta vazia
        """
        return len(self.nos) == 0
