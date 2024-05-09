from ..larg.procura_grafo import ProcuraGrafo
from .fronteira_prioridade import FronteiraPrioridade


class ProcuraMelhorPrim(ProcuraGrafo):
    """
    classe abstrata, que estende doutra classe abstacta, por isso contém um acoplamento
    médio, por existir a aplicação duma arquitetura de software, no caso, 
    a abstração

    Consiste em uma procura best-first, que tem as suas variações, variações estas
    que serão classes que estendem desta classe abstracta

    Args:
        ProcuraGrafo (ProcuraGrafo): estende
    """

    def __init__(self, avaliador):
        """inicia o super construtor da fronteira de prioridade tendo em conta o avaliador
        que possa ser usado (sofre de polimorfismo, por diferenças)

        Args:
            avaliador (_type_): _description_
        """
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
