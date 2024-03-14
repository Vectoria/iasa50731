from lib.sae import Agente, Simulador

from controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.comport_teste import ComportTeste

class AgenteTeste(Agente):
    def __init__():
        comportamento= ComportTeste()
        controlo= ControloReact(comportamento)
        super().__init__(controlo)