from ecr.comportamento import Comportamento
from sae.agente.accao import Accao

class ComportTeste(Comportamento):
    def activar(self, percepcao):
        return Accao(percepcao.direccao)