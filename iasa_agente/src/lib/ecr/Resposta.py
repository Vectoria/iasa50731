class Resposta:
    """
    Classe que representa a resposta aos estimulos

    Que quando ativada, gera uma ação, onde a prioridade varia de intensidade dos estímulos

    """    
    def __init__(self, accao):
        """
        Associação de Accao

        Define que ação que será realizada

        Args:
            accao (Accao): associação
        """       
        
        self._accao=accao

    def activar(self, percepcao,intensidade=0.0):
        """
        A percepção faz a guarda (segurança), em que ativa a Reação e logo vai 
        activar uma resposta, que gera uma ação e seu nível de prioridade 

        Args:
            percepcao (Percepcao): _description_
            intensidade (float, optional): _description_. Defaults to 0.0.

            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA dúvida da intensidade que é 0 ser guarda
            dúvida deste metodo ser apenas para guarda 

        Returns:
            Accao: por causa da percepção, é gerado a ação
        """        
        if percepcao is not None: 
            self._accao.prioridade = intensidade
            return self._accao