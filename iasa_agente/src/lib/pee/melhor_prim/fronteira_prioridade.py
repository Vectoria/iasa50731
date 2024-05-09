from ..mec_proc.fronteira import Fronteira
from heapq import heappush, heappop
# ordenação de ordem menor o heapq


class FronteiraPrioridade(Fronteira):
    """
    Esta classe representa uma fronteira onde a sua prioridade é definida pelo seu avaliador
    Possui um acoplamento forte por extender de uma classe abstracta, mas possuí forte coesão
    Acontece uma fatorização estrutural

    Args:
        Fronteira (Fronteira): extende
    """

    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        """adiciona na lista, o nó no seu lugar por questão de ordem, a ordem é
        definida pela prioridade, calculada pelo avaliador

        Args:
            no (No): nó que desejamos adicionar
        """
        prioridade = self.__avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))

    def remover(self):
        """
        Remove o nó e devolve o mesmo

        Por questão de simplicidade, pomos "_" ao inves de prioridade, uma vez
        que não usamos a variavel da prioridade, então usamos a variavel anonima (pesquisar o nome desta tatica)

        Returns:
            No: devolve o nó removido
        """
        _, no = heappop(self._nos)
        return no
