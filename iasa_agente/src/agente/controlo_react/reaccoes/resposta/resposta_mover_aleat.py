from .resposta_mover import RespostaMover
from sae.ambiente.direccao import Direccao
from random import choice

class RespostaMoverAleat(RespostaMover):
    """
    Classe criada em aula, primeiramente como um desafio redirecionado a nós, os alunos, 
    e de seguida para ser usado no explorar

    Args:
        RespostaMover (RespostaMover): extende
    """    
    def __init__(self):
        """
        é criado uma direção aleatoria, em que a seleção desta aleatoridade consiste em selecionar aleatoriamente~
        a direção existente dos varios tipos de Direção que podem existir (na classe Direccao)
        e logo fazemos a fatorização de maneira a fazer a resposta mover desta direção aleatoria
        """        
        dirrecao_aleatoria= choice(list(Direccao))
        super().__init__(dirrecao_aleatoria)