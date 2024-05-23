from .avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):
    """
    Esta classe apresenta maior coesão por fazer apenas
    a sua função dada pelo seu nome

    Args:
        Avaliador (Avaliador): implementa a interface
    """

    def prioridade(self, no):
        """
        a prioridade consiste em apenas observar o custo do nó

        Args:
            no (No): _description_

        Returns:
            double: retorna o custo do nó
        """
        return no.custo
