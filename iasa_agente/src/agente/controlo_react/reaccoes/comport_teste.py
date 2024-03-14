from lib.ecr.comportamento import Comportamento
from lib.sae.agente.accao import Accao

class ComportTeste(Comportamento):
    def activar(self, percepcao):
        return Accao(percepcao.direccao)