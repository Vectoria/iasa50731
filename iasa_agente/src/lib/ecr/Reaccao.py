from .comportamento import Comportamento
class Reaccao(Comportamento):
    def __init__(self, estimulo, resposta):
        """_summary_

        Args:
            estimulo (Estimulo): _description_
            resposta (Resposta): _description_
        """        
        self.__estimulo=estimulo
        self.__resposta=resposta

    def activar(self, percepcao):
        """
        a percepção, se existir, activa a reação, isso é, detecta um estimulo, em que este dá-nos a 
        intensidade deste estimulo, com esta intensidade, activa uma resposta, que gera uma 
        Ação, tal ação será returnada

        Args:
            percepcao (Percepcao): percepcao para activar/indicar estímulos

        Returns:
            Accao: a Ação é a resposta da Reação
        """        
        
        intensidade= self.__estimulo.detectar(percepcao)
        if intensidade>0:
            return self.__resposta.activar(percepcao,intensidade)
        