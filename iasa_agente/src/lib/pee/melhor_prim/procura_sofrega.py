from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof


class ProcuraSofrega(ProcuraInformada):
    def __init__(self):
        """inicia-se super construtor com o avaliador sofrega
        """
        super().__init__(AvaliadorSof())
