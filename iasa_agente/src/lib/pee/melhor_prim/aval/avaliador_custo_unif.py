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
        Args:
            no (No): serve para por a prioridade em base do seu custo

        Returns:
            double: retorna o custo do nó
        """
        return no.custo
