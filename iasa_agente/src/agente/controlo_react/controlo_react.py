from sae.agente.controlo import Controlo
class ControloReact(Controlo):
    def __init__(self, comportamento):
        self.__comportamento=comportamento
        self.mostrar_per_dir = True
        

    def processar(self,percepcao):
        
        return self.__comportamento.activar(percepcao)