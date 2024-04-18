from pee.prof.procura_profundidade import ProcuraProfundidade


class ProcuraProfLim(ProcuraProfundidade):
    """classe que representa uma procura de profundidade mas com um limite de profundidade
    isso para otimizar

    Args:
        ProcuraProfundidade (_type_): _description_
    """

    def __init__(self, prof_max):
        self.__prof_max = prof_max

    def _expandir(self, problema, no):
        """expande se a profundidade do nó será maior que a profundidade maxima limte

        Args:
            problema (_type_): _description_
            no (_type_): _description_
        """
        return super()._expandir(problema, no) if no.profundidade < self.prof_max else []

    @property
    def prof_max(self):
        """ read only """
        return self.__prof_max

    @prof_max.setter
    def prof_max(self, valor):
        """ set """
        self.__prof_max = valor
