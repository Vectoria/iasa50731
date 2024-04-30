from ecr.prioridade import Prioridade
from .aproximar_dir import AproximarDir
from sae import Direccao


class AproximarAlvo(Prioridade):
    """
    Esta classe é representação de um comportamento com prioridade dinamica,
    em que temos uma lista de comportamentos simples (reações), todos estes são comportamentos estimulos para aproximar numa das 
    direções (norte, sul, este e oeste), respeita o diagrama informal do slide 11

    Contém um acoplamento forte por ser extend

    É uma prioridade dinamica pelo facto de que na lista de comportamentos, cada comportamento gera uma resposta
    a resposta contém a sua prioridade que foi grada pela intensidade da detecção de um estimulo a tal direção, logo
    a direção que causa mais intensidade é aquela que produz uma resposta com mais prioridade, no que resulta a escolha
    prioritaria da ação cujo a resposta tenha mais prioridade no momento


    Args:
        Prioridade (Prioridade): extende
    """
    __comportamentos = [AproximarDir(Direccao.NORTE), AproximarDir(
        Direccao.SUL), AproximarDir(Direccao.ESTE), AproximarDir(Direccao.OESTE)]

    def __init__(self):
        """
        factorização, , usa a classe dos comportamentos compostos para ser incializado,
        introduzindo os comportamentos
        """
        super().__init__(self.__comportamentos)
