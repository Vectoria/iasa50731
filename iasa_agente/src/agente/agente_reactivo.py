from sae import Agente, Simulador
from controlo_react.reaccoes.recolher import Recolher
from controlo_react.controlo_react import ControloReact

class AgenteReactivo(Agente):
    """classe para dar run ao código, no caso, queremos testar o comportamento Recolher

    Args:
        Agente (Agente): extende
    """    
    def __init__(self):
        comportamento= Recolher()
        controlo= ControloReact(comportamento)
        super().__init__(controlo)

""" Executar o modulo main """
if __name__ == "__main__":
    #agenteTeste= AgenteTeste()
    Simulador(1, AgenteReactivo()).executar()