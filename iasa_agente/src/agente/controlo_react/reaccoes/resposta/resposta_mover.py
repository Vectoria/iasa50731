from ecr.resposta import Resposta
from sae import Accao


class RespostaMover(Resposta):
    """
    Acoplação alto por extender
    factorização estrutural por ser herança
    Classe que é uma resposta sobre movimento do agente (é observado empiricamente no jogo em interface gráfica)
    Tal classe serve também para guardar a informação das ações, para depois ativa-las

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
