from abc import ABC, abstractmethod


class ModeloPDM(ABC):

    @abstractmethod
    def S(self):
        """ conjunto de estados do mundo """

    @abstractmethod
    def A(self, s):
        """ conjunto de ações possiveis no estado dentro de estados do mundo """

    @abstractmethod
    def T(self, s, a, sn):
        """ probabilidade de transição de s para s' através de a """

    @abstractmethod
    def R(self, s, a, sn):
        """ recompensa esperada na transição de s para s' através de a """

    @abstractmethod
    def suc(self, s, a):
        """ sucessor """
