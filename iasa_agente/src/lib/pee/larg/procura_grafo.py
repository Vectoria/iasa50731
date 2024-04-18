from mec_proc.mecanismo_procura import MecanismoProcura


class ProcuraGrafo(MecanismoProcura):
    def _iniciar_memoria(self):
        """programação por diferenças, em que existe uma facotrização

        Returns:
            _type_: _description_
        """

        super()._iniciar_memoria()
        self._explorados = []

    def _memorizar(self, no):
        estado = no.estado
        if self._manter(no):
            self._fronteira.inserir(no)
            self._explorados[estado] = no

        return super()._memorizar(no)

    def _manter(self, no):
        """indicamos se o nó é para manter ou não

        Args:
            no (_type_): _description_
        """
        return no.estado not in self._explorados
