from mec_proc.mecanismo_procura import MecanismoProcura


class ProcuraGrafo(MecanismoProcura):
    """
    Alto acoplamento por extender, tmabém é classe abstracta

    A classe tem o proposito de não desperdicar os recursos (sejam estes o tempo ou memoria) quando ocorre algum estado repetido na expansão
    de nó
    Quando encontra um nó repetido, verifica se este nó possuí um menor custo, se for, elimina-se o outro nó, caso não or, elimina o nó repetido

    Args:
        MecanismoProcura (MecanismoProcura): extende
    """

    def _iniciar_memoria(self):
        """
        Programação por diferenças, em que existe uma facotrização
        Cria uma lista para os nós fechados
        """

        super()._iniciar_memoria()
        self._explorados = []

    def _memorizar(self, no):
        """
        insere o nó na fronteira e guarda na lista de nós fechados se este for mantido

        Args:
            no (_type_): _description_

        """
        estado = no.estado
        if self._manter(no):
            self._fronteira.inserir(no)
            self._explorados[estado] = no

        return super()._memorizar(no)

    def _manter(self, no):
        """indicamos se o nó é para manter ou não
        Para esta fim, verifica-se se o nó esta na lista de nós fechados

        Args:
            no (_type_): _description_
        """
        return no.estado not in self._explorados
