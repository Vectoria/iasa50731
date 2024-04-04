from ecr.resposta import Resposta
from sae.ambiente.direccao import Direccao
from sae.agente.accao import Accao


class RespostaEvitar(Resposta):
    def __init__(self, direccao=Direccao.ESTE):
        self.__direcao = direccao
        self.__dirrecoes = list(Direccao)

        """ direccoes_evitar = {Direccao.NORTE: Direccao.SUL, Direccao.ESTE: Direccao.OESTE,
                            Direccao.SUL: Direccao.NORTE, Direccao.OESTE: Direccao.ESTE}
        super().__init__(direccoes_evitar.get(direccao)) """

    def activar(self, percepcao, intensidade=0):
        if percepcao.contacto_obst(self.__direcao):

            self.__direccao_livre(percepcao)
        else:

            return Accao(self.__direcao)

    def __direccao_livre(self, percepcao):
        dir_vigente = self.__direcao
        for i in range(len(self.__dirrecoes)):
            if percepcao.contacto_obst(self.__dirrecoes[i]):
                dir_vigente = self.__dirrecoes[i]
                break
        return Accao(dir_vigente)
