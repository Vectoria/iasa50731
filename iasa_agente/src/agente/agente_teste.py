from sae import Agente, Simulador

from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.comport_teste import ComportTeste


class AgenteTeste(Agente):
    def __init__(self):
        comportamento = ComportTeste()
        controlo = ControloReact(comportamento)
        super().__init__(controlo)


""" Executar o modulo main """
if __name__ == "__main__":
    """ 
    Aconteceu um erro na entrega da semana 4, onde ao inves de 
    executar o simulador, executava era o agente teste
    """
    Simulador(1, AgenteTeste()).executar()
