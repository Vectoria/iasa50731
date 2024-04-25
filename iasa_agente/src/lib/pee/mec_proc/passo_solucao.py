from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador


@dataclass
class PassoSolucao():
    """
    define uma classe de dados, ou seja, serve para fazer iteração dos passos, 
    armazenando o estado e o operador
    """
    estado: Estado
    operador: Operador
