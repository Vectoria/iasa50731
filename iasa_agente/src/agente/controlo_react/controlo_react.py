from sae import Controlo


class ControloReact(Controlo):
    """
    Para uma arquitetura de um agente reactivo, é criado esta classe, Controlo Reactivo

    Extende de Controlo que é a modularização do processamento interno da 
    arquitetura agente 

    Acoplamento alto devido a classe ser extendida, herança (factorização estrutural),
    uma vez que a classe, ControloReact, é um tipo de Controlo

    Args:
        Controlo (Controlo): extensão
    """

    def __init__(self, comportamento):
        """
        inicia um controlo reactivo, do qual tem o seu comportamento e já precepciona a direção

        Erro na entrega da semana 4, onde o self.mostrar_per_dir estava com aspas com o valor de True
        ao inves de afetar

        Args:
            comportamento (Comportamento): modulo comprotamental, agregação
        """
        self.__comportamento = comportamento
        self.mostrar_per_dir = True

    def processar(self, percepcao):
        """
        ativa o comportamento, ou seja, gera uma resposta que cria uma ação

        Args:
            percepcao (Percepção): percepção para ativar a reação

        Returns:
            Accao: a reação gera uma resposta que é uma ação
        """
        return self.__comportamento.activar(percepcao)
