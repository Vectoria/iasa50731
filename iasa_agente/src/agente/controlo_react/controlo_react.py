from lib.sae.agente.controlo import Controlo
class ControloReact(Controlo):
    def __init__(self, comportamento):
        self.__comportamento=comportamento

    def processar(self,percepcao):
        self.mostrar_per_dir(True)
        return self.__comportamento.activar(percepcao)