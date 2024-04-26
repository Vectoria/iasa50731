from .estado_contagem import EstadoContagem
from mod.problema import Problema
from .operador_incremento import OperadorIncremento


class ProblemaContagem(Problema):
    """
    incia um problema, onde começa com um valor inicial (estado), possui incrementos (operadores)
    do qual são necessarios para chegar ao valor final (estado objetivo)

    Args:
        Problema (Problema): extende
    """

    def __init__(self, valor_inicial, valor_final, incrementos):
        """
        Inicia atráves de um super (factorização), o estado inicial com o valor inicial e os operadores de incremento,
        além de declarar o valor final

        É usado uma compressão de lista no operador incremento, uma vez que podem haver varios tipos de incrementos
        """
        super().__init__(EstadoContagem(valor_inicial), [
            OperadorIncremento(inc) for inc in incrementos])
        self.__valor_final = valor_final

    def objetivo(self, estado):
        """o objetivo é quando o valor é maior ou igual ao valor final
        """
        return estado.valor >= self.__valor_final
