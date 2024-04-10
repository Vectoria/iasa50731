from ecr.resposta import Resposta
from sae.agente.accao import Accao


class RespostaMover(Resposta):
    """
    Acoplação alto
    Classe que é uma resposta sobre movimento
    Tal classe serve para guardar a informação das ações

    Args:
        Resposta (Resposta): Extende
    """

    def __init__(self, direccao):
        """
        Por ser uma resposta que move, então criamos uma ação que 
        tenha uma direção dada pelo utilizador, ou seja, uma ação de movimento

        Args:
            direccao (Direccao): direção que predente ir, dependencia
        """
        super().__init__(Accao(direccao))
