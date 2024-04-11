from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador


@dataclass
class PassoSolucao():
    """
    define uma classe de dados
    """
    estado: Estado
    operador: Operador
