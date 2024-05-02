from .avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):
    """
    Esta classe apresenta maior coesão por fazer apenas
    a sua função dada pelo seu nome

    Args:
        Avaliador (_type_): _description_
    """

    def prioridade(self, no):
        """_summary_

        Args:
            no (_type_): _description_

        Returns:
            double: _description_
        """
        return no.custo
