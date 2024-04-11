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
        Comportamento (Comportamento): implementa a interface
    """

    def activar(self, percepcao):
        """
        Observamos a direção atual com a percepção, com tal direção vemos qual será a proxima,
        de acordo com os ponteiros do relógio, para a finalidade, criamos um dicionario com uma
        key de uma direção e a sua value é a proxima direção.
        Com a proxima direção, criamos uma resposta de movimento e ativamos a mesma


        Args:
            percepcao (Percepcao): associação

        Returns:
            Accao: fatorização onde acontece a ativação da ação
        """
        dir_atual = percepcao.direccao
        direccoes_rodar = {Direccao.NORTE: Direccao.ESTE, Direccao.ESTE: Direccao.SUL,
                           Direccao.SUL: Direccao.OESTE, Direccao.OESTE: Direccao.NORTE}

        resposta = RespostaMover(direccoes_rodar.get(dir_atual))

        return resposta.activar(percepcao)
        ""
