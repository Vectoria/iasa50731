from sae import Elemento


class MecDelib():

    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):
        """
        o mecanismo delibera, onde ve todos os objetivos no mundo, que no caso são alvos

        Returns:
            _type_: _description_
        """
        estados = self.__modelo_mundo.obter_estados()
        objetivos = []
        for i in range(estados):
            elemento = self.__modelo_mundo.obter_elemento(estados(i))
            if elemento == Elemento.ALVO:
                objetivos.append(elemento)

        return objetivos
