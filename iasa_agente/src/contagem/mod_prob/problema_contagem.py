from .estado_contagem import EstadoContagem
from mod.problema import Problema
from .operador_incremento import OperadorIncremento


class ProblemaContagem(Problema):
    def __init__(self, valor_inicial, incrementos, valor_final):
        super().__init__(EstadoContagem(valor_inicial), [
            OperadorIncremento(inc) for inc in incrementos])
        self.__valol_Final = valor_final

    def objetivo(self, estado):
        """o objetivo é quando o valor é maior ou igual ao valor final
        """
        return estado.valor >= self.__valor_final
