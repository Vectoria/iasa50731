from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae import Agente, Simulador
from controlo_delib.controlo_delib import ControloDelib


class AgenteDelibPEE(Agente):

    def __init__(self):
        planeador = PlaneadorPEE()
        controlo = ControloDelib(planeador)
        super().__init__(controlo)


""" Executar o modulo main """
if __name__ == "__main__":
    Simulador(4, AgenteDelibPEE()).executar()
