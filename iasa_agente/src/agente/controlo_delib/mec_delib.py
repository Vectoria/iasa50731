from sae import Elemento


class MecDelib():

    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):
        estados = self.__modelo_mundo.obter_estados()
        objetivos = []
        for i in range(estados):
            elemento = self.__modelo_mundo.obter_elemento(estados(i))
            if elemento == Elemento.ALVO:
                objetivos.append(elemento)

        return objetivos
