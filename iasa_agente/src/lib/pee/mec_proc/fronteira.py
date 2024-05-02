from abc import ABC, abstractmethod


class Fronteira(ABC):
    """
    Possui um acoplamento ligeiramente for por ter agregação

    Classe que representa a Fronteira, estrutura de dados com relação de ordem, em que
    determina estratégia de controlo da procura, ou seja, permite controlar os nós que estão a ser expandidos/processados
    Os nós presentes na fronteira são abertos (nós que foram gerados mas ainda não foram expandidos)

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
        self._nos = []

    @abstractmethod
    def inserir(self, no):
        """ metodo abstracto, deixado para ser aplicado para as fronteiras FIFO e LIFO """

    def remover(self):
        """
        remove o primeiro item, por ser fronteira de exploração, onde o primeiro item sempre sai

        Returns:
            list: retorna a lista sem o primeiro elemento
        """
        return self._nos.pop(0)

    @property
    def vazia(self):
        """verifica se a lista esta vazia, ou seja, se a fronteira for vazia 
        """
        return len(self._nos) == 0
