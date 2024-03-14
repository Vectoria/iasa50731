class Resposta:
    def __init__(self, accao):
       # raise NotImplementedError
        
        self._accao=accao

    def activar(self, percepcao,intensidade=0.0):
        """
        A percepção faz a guarda, em que ativa a Reação e logo vai 
        activar uma resposta, que gera uma ação

        Args:
            percepcao (_type_): _description_
            intensidade (float, optional): _description_. Defaults to 0.0.

        Returns:
            _type_: _description_
        """        
        if percepcao is not None: 
            self._accao.prioridade = intensidade
            return self._accao
        #raise NotImplementedError