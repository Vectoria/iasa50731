from abc import ABC, abstractclassmethod

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao


class MecanismoProcura(ABC):
    def __init__(self, fronteira):
        self._fronteira = fronteira

    def _iniciar_memoria(self):
        self._fronteira.iniciar()

    @abstractclassmethod
    def _memorizar(self, no):
        ""

    def procurar(self, problema):
        """
        segue o slide 9 do capitulo pee

        Args:
            problema (Problema): 

        Returns:
            _type_: _description_
        """
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            if problema.objetivo(no.estado):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)

    def _expandir(self, problema, no):
        """
        segue o slide 10 do capitulo pee

        Args:
            problema (_type_): _description_
            no (_type_): _description_

        Returns:
            list: _description_
        """
        sucessores = []
        estado = no.estado
        for operator in self.problema.operadores:
            estado_suc = operator.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operator.custo(estado, estado_suc)
                no_sucessor = No(estado_suc, operator, no, custo)
                sucessores.append(no_sucessor)
        return sucessores
