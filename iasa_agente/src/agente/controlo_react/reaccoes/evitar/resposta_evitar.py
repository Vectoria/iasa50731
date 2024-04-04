from ..resposta.resposta_mover import RespostaMover
from sae.ambiente.direccao import Direccao
from sae.agente.accao import Accao
from random import choice


class RespostaEvitar(RespostaMover):
    """


    Args:
        RespostaMover (RespostaMover): extend, por ser imitir que move com a resposta
    """

    def __init__(self, direccao=Direccao.ESTE):
        """_summary_

        Args:
            direccao (_type_, optional): _description_. Defaults to Direccao.ESTE.
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
            intensidade (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        if percepcao.contacto_obst(self._accao.direccao):

            # := é testar a função e ver se retorna algo
            if direccao_livre := self.__direccao_livre(percepcao):
                # resposta com memoria, por
                self._accao.direccao = direccao_livre

            else:
                return None
        # não precisa do else já que o fluxo coicide no que vai retornar
        return super().activar(percepcao, intensidade)

    def __direccao_livre(self, percepcao):
        dirrecoes_livre = [direccao for direccao in self.__direcoes
                           if not percepcao.contacto_obst(direccao)]
        if dirrecoes_livre:
            return choice(dirrecoes_livre)
