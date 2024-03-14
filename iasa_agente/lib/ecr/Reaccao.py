class Reaccao:
    def __init__(self, estimulo, resposta):
        self.estimulo=estimulo
        self.resposta=resposta
    def activar(self, percepcao):
        raise NotImplementedError