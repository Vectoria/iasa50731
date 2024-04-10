from ecr.comportamento import Comportamento
from sae.ambiente.direccao import Direccao
from ..resposta.resposta_mover import RespostaMover


class ExplorarRodar(Comportamento):
    """
    Classe que extende de Comportamento

    A classe foi criada em aula, como um desafio aos alunos, 
    basicamente é um comportamento de rodar, como diz o nome, 
    no sentido dos ponteiros do relogio

    Args:
        Comportamento (_type_): _description_
    """

    def activar(self, percepcao):
        dir_atual = percepcao.direccao
        direccoes_rodar = {Direccao.NORTE: Direccao.ESTE, Direccao.ESTE: Direccao.SUL,
                           Direccao.SUL: Direccao.OESTE, Direccao.OESTE: Direccao.NORTE}

        resposta = RespostaMover(direccoes_rodar.get(dir_atual))

        return resposta.activar(percepcao)
        ""
