from ..larg.procura_grafo import ProcuraGrafo
from .fronteira_prioridade import FronteiraPrioridade


class ProcuraMelhorPrim(ProcuraGrafo):

    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador

    def _manter(self, no):
        """
        Mantém o nó se fizer o super da classe (se o nó não esta na lista)
        ou se tem o nó na lista mas tal nó tem um custo menor

        Nem precisava do ".custo" nos nós (por existir a comparação na classe Nó), 
        mas para entender melhor ao ver o código, ficou mantido

        Args:
            no (No): _description_

        Returns:
            _type_: _description_
        """
        return super()._manter(no) or \
            no.custo < self._explorados[no.estado].custo
