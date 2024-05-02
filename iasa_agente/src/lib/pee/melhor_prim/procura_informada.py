from .procura_melhor_prim import ProcuraMelhorPrim


class ProcuraInformada(ProcuraMelhorPrim):
    """
    Classe ao qual redifine apenas o método procurar, dinamicamente

    Args:
        ProcuraMelhorPrim (_type_): extend
    """

    def procurar(self, problema, heuristica):
        """
        heuristica serve para configurar o avaliador
        seguidamente fazemos o super do método

        Args:
            problema (_type_): _description_
            heuristica (_type_): _description_

        Returns:
            _type_: _description_
        """
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
