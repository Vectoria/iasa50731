from abc import ABC, abstractclassmethod


class Fronteira(ABC):
    """
    Classe que representa a classe Fronteira

    Args:
        ABC (ABC): para a classe ser abstracta
    """

    def __init__(self):
        self.iniciar()

    def iniciar(self):
        """inicia uma lista vazia de nós, que mais tarde recebera outros nós nas classes que extendem desta classe
        """
        self.nos = []

    @abstractclassmethod
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
