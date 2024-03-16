""" interface, ou seja, um contrato funcional
    usamos o import para fazer a classe abstracta/interface"""
from abc import ABC, abstractclassmethod

""" a classe recebe o ABC para transformar em abstracto/interface
    de seguida, em cada classe que ainda n foi implementado, escrevemos um @abstractclassmethod
    e escrevemos no metodo uma string, de maneira a não dar erro (como um raise NotImplementedError) """

class Estimulo(ABC):
    @abstractclassmethod
    def detectar(self, percepcao):
        "Detectar estimulo"