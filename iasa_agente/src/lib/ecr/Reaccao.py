from .comportamento import Comportamento


class Reaccao(Comportamento):
    """ implementa a interface Comportamento
    isso se da ao facto de que a reação é um tipo 
    de comportamento, neste caso, simples

    Acoplamento médio, por ter agregação

    Args:
        Comportamento (Comportamento): implementa a interface
    """

    def __init__(self, estimulo, resposta):
        """
        Contém agregação de Estimulo e Resposta

        Uma vez que a reação define a modulação das associações entre o estímulo e a resposta
        Args:
            estimulo (Estimulo): agregação
            resposta (Resposta): agregação
        """
        self.__estimulo = estimulo
        self.__resposta = resposta

    def activar(self, percepcao):
        """
        Obedece ao diagrama de sequencias, presente no slide 4
        A percepção, se existir, activa a reação, isso é, detecta um estimulo, em que este dá-nos a 
        intensidade deste estimulo, com esta intensidade, activa uma resposta, que gera uma 
        Ação, tal ação será returnada


        Args:
            percepcao (Percepcao): percepcao para activar/indicar estímulos

        Returns:
            Accao: a Ação é a resposta da Reação
        """

        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            return self.__resposta.activar(percepcao, intensidade)
