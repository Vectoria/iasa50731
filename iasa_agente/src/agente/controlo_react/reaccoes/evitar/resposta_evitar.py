from ..resposta.resposta_mover import RespostaMover
from sae import Direccao
from random import choice


class RespostaEvitar(RespostaMover):
    """
    Modifica a direção atual para uma que esteja livre

    Args:
        RespostaMover (RespostaMover): extend, por ser imitir que move com a resposta
    """

    def __init__(self, direccao=Direccao.ESTE):
        """
        Cria-se uma lista de todas as direções e inicia a direção para ter a ação

        Args:
            direccao (Direccao, optional): associação. Defaults to Direccao.ESTE.
        """
        self.__direcoes = list(Direccao)
        super().__init__(direccao)

    def activar(self, percepcao, intensidade=0):
        """
        É a representação em codigo do diagrama de atividade presente no slide 14

        Verificamos se existe algum contacto com o obstáculo, se sim vemos se existe alguma 
        direção livre, se não tiver, retorna vazio (não faz nada), se tiver, apenas mudamos 
        a direção atual para a direção que esteja livre, de seguida, também para o caso de 
        não contactar com algum obstáculo, retorna o super do activar da classe RespostaMover


        Args:
            percepcao (Percepcao): usado para saber se esta em contacto com obstaculo,
            para ver uma direção livre e também serve de fatorização (o super)
            intensidade (int, optional): Defaults to 0.

        Returns:
            Accao: associação, ativa a resposta, produzindo uma ação de mover
            a outra direção que esteja livre
        """
        if percepcao.contacto_obst(self._accao.direccao):

            # :=, walrus operator, é testar a função e ver se retorna algo, ~
            # se retornar, cumpriu a condição
            if direccao_livre := self.__direccao_livre(percepcao):
                # resposta com memoria
                self._accao.direccao = direccao_livre

            else:
                return None
        # não precisa do else já que o fluxo coicide no que vai retornar
        return super().activar(percepcao, intensidade)

    def __direccao_livre(self, percepcao):
        """
        Acontece uma list comprehension, onde a lista tem todas as direções que
        sejam livres, de seguida escolhe aleatoriamente uma direção livre da lista 


        Args:
            percepcao (Percepcao): associação, util para saber se esta em 
            contacto com algum obstaculo

        Returns:
            Direcao: associação, retorna uma direção aleatoria que seja livre
        """
        dirrecoes_livre = [direccao for direccao in self.__direcoes
                           if not percepcao.contacto_obst(direccao)]
        if dirrecoes_livre:
            return choice(dirrecoes_livre)
