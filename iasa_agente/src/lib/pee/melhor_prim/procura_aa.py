from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA


class ProcuraAA(ProcuraInformada):
    def __init__(self):
        """inicia-se o contrutor com a super classe com o avaliador do tipo a*
        """
        super().__init__(AvaliadorAA())
