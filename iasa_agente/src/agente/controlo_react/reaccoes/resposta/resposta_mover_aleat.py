from .resposta_mover import RespostaMover
from sae import Direccao
from random import choice


class RespostaMoverAleat(RespostaMover):
    """
    Alto acoplamento por extender   
    Factorização estrutural por ser herança
    Classe criada em aula, primeiramente como um desafio redirecionado a nós, os alunos, 
    e de seguida, tal classe serve para ser usado na classe Explorar (boa coesão),
    também serve para aumentar a coesão (distribuí o papel que era suposto o 
    RespsotaMover ter, para esta classe)

    Args:
        RespostaMover (RespostaMover): extende
    """

    def __init__(self):
        """
        É criado uma direção aleatoria, para tal acontece uma seleção aleatoria de uma das direções
        existente nos tipos de Direção que podem existir (na classe Direccao, ou seja, Norte, Sul, Este e Oeste)
        e logo fazemos a fatorização de maneira a fazer a resposta mover desta direção aleatoria
        """
        dirrecao_aleatoria = choice(list(Direccao))
        super().__init__(dirrecao_aleatoria)
