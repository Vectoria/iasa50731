from ..mec_proc.mecanismo_procura import MecanismoProcura


class ProcuraGrafo(MecanismoProcura):
    """
    Alto acoplamento por extender, tmabém é classe abstracta

    É um mecanismo de procura não informada, uma vez que não usa o domínio do problema para guiar a procura

    A classe tem o proposito de não desperdicar os recursos (sejam estes o tempo ou memoria) quando ocorre algum estado repetido na expansão
    de nó
    Quando encontra um nó repetido, verifica se este nó possuí um menor custo, se for, elimina-se o outro nó, caso não, elimina o nó repetido

    Args:
        MecanismoProcura (MecanismoProcura): extende
    """

    def _iniciar_memoria(self):
        """
        Programação por diferenças, em que existe uma facotrização
        Cria uma lista para os nós fechados

        Erro em por uma lista ao inves de dicionario, corrigido no dia 2 de Maio
        """
        super()._iniciar_memoria()
        self._explorados = {}

    def _memorizar(self, no):
        """
        insere o nó na fronteira e guarda na lista de nós fechados se este for mantido

        Devido ao erro de ter uma lista ao inves de dicionario, mudou-se o inserimento do nó, usando o update

        Erro da semana 8, no qual fazia mal a sintaxe do metodo update (para inserir keys e values), e também
        dava return do super do metodo (o que não faz sentido, uma vez que o metodo é abstrato), corrigido no dia 17 de maio

        Args:
            no (_type_): _description_

        """
        estado = no.estado
        if (self._manter(no)):
            self._fronteira.inserir(no)
            self._explorados.update({estado: no})
            # self._explorados[estado] = no

    def _manter(self, no):
        """indicamos se o nó é para manter ou não
        Para esta fim, verifica-se se o nó esta na lista de nós fechados

        Args:
            no (_type_): _description_
        """
        return no.estado not in self._explorados
