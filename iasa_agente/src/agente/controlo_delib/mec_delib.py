from sae import Elemento


class MecDelib():

    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):
        """
        o mecanismo delibera, onde ve todos os objetivos no mundo, que no caso são alvos,
        do mais perto ao longe

        Erro na semana 10, onde percorria o ciclo for de um objeto não numerico,
        precisou-se usar len para er a quantidade de estados, corrigido no dia 16 de maio

        No mesmo dia, faz um sort dos objetivos, do mais perto para o mais longe,
        onde a avaliação para este sort é a distancia no modelo mundo 

        Returns:
            lista: objetivos, ou seja, todos os elementos que são alvos
        """
        objetivos = [estado for estado in self.__modelo_mundo.obter_estados()
                     if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        """ estados = self.__modelo_mundo.obter_estados()
        objetivos = []
        for i in range(len(estados)):
            elemento = self.__modelo_mundo.obter_elemento(i)
            if elemento == Elemento.ALVO:
                objetivos.append(elemento) """
        if objetivos:
            objetivos.sort(key=self.__modelo_mundo.distancia)
            return objetivos
