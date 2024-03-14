from sae import Accao
class Resposta:
    def __init__(self, accao):
        raise NotImplementedError
        #self.accao=accao

    def activar(self, percepcao,intensidade=0):
        raise NotImplementedError