from .avaliador_heur import AvaliadorHeur


class AvaliadorAA(AvaliadorHeur):
    """
    classe a qual faz a avaliação da procura A*
    a qual o f(n)= g(n) + h(n)


    Args:
        AvaliadorHeur (_type_): _description_
    """

    def prioridade(self, no):
        """minimização do custo global

        Args:
            no (_type_): _description_

        Returns:
            _type_: _description_
        """
        return no.custo + self._heuristica.h(no.estado)
