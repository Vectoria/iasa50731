from .avaliador_heur import AvaliadorHeur


class AvaliadorAA(AvaliadorHeur):
    """
    classe a qual faz a avaliação da procura A*
    a qual o f(n)= g(n) + h(n)


    Args:
        AvaliadorHeur (AvaliadorHuer): estende da classe abstracta
    """

    def prioridade(self, no):
        """minimização do custo global

        Returns:
            double: retorna o valor do no junto com a heuristica
        """
        return no.custo + self._heuristica.h(no.estado)
