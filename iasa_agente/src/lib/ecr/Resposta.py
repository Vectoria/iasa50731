class Resposta:
    """
    Classe que representa a resposta aos estimulos
    Pode ser usado para comportamento fixo

    Que quando ativada, gera uma ação, onde a prioridade varia de intensidade dos estímulos

    Fraco Acoplamento

    """

    def __init__(self, accao):
        """
        Associação de Accao

        Define que ação que será realizada

        Args:
            accao (Accao): associação
        """

        self._accao = accao

    def activar(self, percepcao, intensidade=0.0):
        """
        A percepção e ativa a Reação, detecta se tem estimulos, se tiver, gera uma intensidade e activa a resposta, gerando uma ação e sua prioridade

        Caso não tenha detectado estimulos (isso é, quando a intensidade é 0.0), faz a guarda e activa logo a resposta, gerando a ação

        Args:
            percepcao (Percepcao): Para ativar a reação
            intensidade (float, optional): caso haja intensidade, gera um número de prioridade da ação, caso seja default,
            acontece a guarda e o número de prioridade da ação é 0 


        Returns:
            Accao: por causa da percepção, é gerado a ação
        """
        if percepcao is not None:
            self._accao.prioridade = intensidade
            return self._accao
