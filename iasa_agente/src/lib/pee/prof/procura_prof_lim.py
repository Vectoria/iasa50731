from .procura_profundidade import ProcuraProfundidade


class ProcuraProfLim(ProcuraProfundidade):
    """
    Possuí forte acoplamento por extender

    Classe que representa uma procura de profundidade mas com um limite de profundidade maxima
    isso serve para otimizar os recursos, seja por tempo ou por espaço

    Args:
        ProcuraProfundidade (ProcuraProfundidade): extende
    """

    def __init__(self, prof_max):
        """
        erro da semana 8, onde falatava o super construtor, corrigido no dia 20 de junho

        Args:
            prof_max (int): tamanho limite para a profundidade
        """
        super().__init__()
        self.__prof_max = prof_max

    def _expandir(self, problema, no):
        """
        Expande, atraves de fatorização,se a profundidade do nó será menor que
        a profundidade maxima limte

        Erro cometido na semana 7, onde o comentario estava escrito que se a profundidade
        do nó fosse MAIOR que a profundidade maxima, este iria expandir

        Args:
            problema (Problema): para usar os operadores
            no (Nó): ver a profundidade do nó e expandir este se possível
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
