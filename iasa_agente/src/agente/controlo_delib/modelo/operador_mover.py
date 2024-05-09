import math
from .estado_agente import EstadoAgente
from mod.operador import Operador
from sae import Accao


class OperadorMover(Operador):
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__accao = Accao(direccao)
        self.__ang = self.__accao.ang
        super().__init__()

    def aplicar(self, estado):
        """  simula a execução da ação, slide 5, acontece uma translação geometrica """
        nova_posicao = self.__translacao(
            estado.posicao, self.accao.passo, self.ang)
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado

    def custo(self, estado, estado_suc):
        return math.dist(estado.posicao, estado_suc.posicao)

    def __translacao(self, posicao, distancia, angulo):
        """
        metodo criado em aula do dia 9 de maio, segue o slide 5

        Apesar que seja representado no metodo cartesiano, o y sera 
        negativo porque o Pygame considera o crescimentod o y de baixo para cima

        acontece a estruturação de objetos para aceder a tuplos

        Args:
            posicao (_type_): _description_
            distancia (_type_): _description_
            angulo (_type_): _description_

        Returns:
            _type_: _description_
        """
        x, y = posicao
        dx = round(distancia * math.cos(angulo))
        dy = -round(distancia * math.sin(angulo))
        nova_posicao = x+dx, y+dy
        return nova_posicao

    @property
    def accao(self):
        return self.__accao

    @property
    def ang(self):
        return self.__ang
