import math
from .estado_agente import EstadoAgente
from mod.operador import Operador
from sae import Accao


class OperadorMover(Operador):
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__accao = Accao(direccao)
        super().__init__()

    def aplicar(self, estado):
        """  
        aplica a ação da translação do agente, de seguida verifica-se
        se esta posição esta no modelo do mundo, se estiver, retorna a posição

        """
        nova_posicao = self.__translacao(
            estado.posicao, self.accao.passo, self.ang)
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado

    def custo(self, estado, estado_suc):
        """_summary_

        Args:
            estado (Estado): posição atual
            estado_suc (Estado): posição seguinte

        Returns:
            float: diferença entre as posições
        """
        return math.dist(estado.posicao, estado_suc.posicao)

    def __translacao(self, posicao, distancia, angulo):
        """
        metodo criado em aula do dia 9 de maio, em que o motivo da sua criação da-se o facto de que
        podemos modularizar mais o metodo, fazendo como que os metodos cheguem a quase fazer uma função (melhor coesão)


        Segue o slide 5, apesar que seja representado no metodo cartesiano, o y sera 
        negativo porque o Pygame considera o crescimentod o y de baixo para cima

        acontece a estruturação de objetos para aceder a tuplos

        Args:
            posicao (Posicao): posição atual
            distancia (float): distancia aplicada
            angulo (float): o angulo, fazendo como que o ambiente não seja bilateral 2d

        Returns:
            Posicao: novas coordenadas da posição
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
        return self.__accao.dirrecao.value
        # return self.__ang
