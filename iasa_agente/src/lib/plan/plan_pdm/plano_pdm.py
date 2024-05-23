from ..plano import Plano


class PlanoPDM(Plano):
    """
    Representa o plano das propriedades de markov

    Args:
        Plano (Plano): implementa a interface
    """

    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        """
        retorna a ação associada ao estado no dicionario politica, se
        a politica existir

        Args:
            estado (Estado): o estado procura a ação no dicionario

        Returns:
            Accao: ação do estado
        """
        if self.__politica:
            return self.__politica.get(estado)

    def mostrar(self, vista):
        for estado, valor in self.__utilidade.items():
            vista.mostrar_valor_posicao(estado.posicao, valor)

        for estado, accao in self.__politica.items():
            vista.mostrar_vector(estado.posicao, accao.ang)
        # print(self.__utilidade)
