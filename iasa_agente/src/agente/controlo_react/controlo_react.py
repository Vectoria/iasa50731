from sae.agente.controlo import Controlo
class ControloReact(Controlo):
    """
    Para uma arquitetura de um agente reactivo, é criado esta classe, Controlo Reactivo

    Extende de Controlo que é a modularização do processamento interno da 
    arquitetura agente 
    
    Acoplamento alto devido a classe ser extendida, herança (factorização estrutural),
    uma vez que a classe, ContrloReact, é um tipo de Controlo

    Args:
        Controlo (Controlo): extensão
    """    
    def __init__(self, comportamento):
        """_summary_

        Args:
            comportamento (Comportamento): agregação
        """        
        self.__comportamento=comportamento
        self.mostrar_per_dir = True
        

    def processar(self,percepcao):
        """_summary_

        Args:
            percepcao (Percepção): _description_

        Returns:
            Accao: _description_
        """        
        return self.__comportamento.activar(percepcao)