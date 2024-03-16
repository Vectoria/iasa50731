class Resposta:
    def __init__(self, accao):
        """
        Resposta, associação de Accao

        Args:
            accao (Accao): 
        """       
        
        self._accao=accao

    def activar(self, percepcao,intensidade=0.0):
        """
        A percepção faz a guarda (segurança), em que ativa a Reação e logo vai 
        activar uma resposta, que gera uma ação

        Args:
            percepcao (_type_): _description_
            intensidade (float, optional): _description_. Defaults to 0.0.

        Returns:
            Accao: por causa da percepção, é gerado a ação
        """        
        if percepcao is not None: 
            self._accao.prioridade = intensidade
            return self._accao