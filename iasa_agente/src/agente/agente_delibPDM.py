
from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Agente, Simulador


class AgenteDelibPDM(Agente):
    def __init__(self):
        """
        o planeador das propriedades de Markov teve a alteração da gama a 0.98, 
        apenas para o cenario 4, uma vez que se fosse pela gama default, o agente
        iria ficar parado processando
        """
        planeador = PlaneadorPDM(gama=0.98)
        controlo = ControloDelib(planeador)
        super().__init__(controlo)


""" Executar o modulo main """
if __name__ == "__main__":
    Simulador(4, AgenteDelibPDM()).executar()
