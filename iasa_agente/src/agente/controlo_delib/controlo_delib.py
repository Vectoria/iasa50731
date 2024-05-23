from .mec_delib import MecDelib
from .modelo.modelo_mundo import ModeloMundo
from sae import Controlo


class ControloDelib(Controlo):
    """
    A classe representa um processamento interno que corresponde a um ciclo de tomada de decisão e ação planeados e deliberado, ou seja,
    um controlo deliberativo de uma arquitetura deliberativa, em que possui um mecanismo de deliberação,
    um planeador, assim como a sua representação no mundo e interação com o mesmo

    Possuí alta acoplamento, por ter composição com o planeador, mecanismo deliberação e modelo mundo

    Args:
        Controlo (Controlo): estende deste
    """

    def __init__(self, planeador):
        """
        erro da semana 10, tinha um underscore depois da variavel modelo_mundo, 
        corrigido no dia 16 de maio

        Args:
            planeador (Planeador): o planeador para gerar planos
        """
        self.__planeador = planeador
        self.__objetivos = []
        self.__modelo_mundo = ModeloMundo()
        self.__plano = None
        self.__controlo = MecDelib(self.__modelo_mundo)
        # super().__init__()

    def processar(self, percepcao):
        """
        O método é a representação do processo geral de tomada de decisão e ação

        segue o diagrama do slide 6, em que recebe a percepção, para reconhecer o mundo externo,
        verifica se não existe um plano ou se houve alguma alteração no mundo, se verificar
        esta condição, então acontece uma atualização de objetivos e cria um novo plano,
        esta condição serve para termos uma eficiencia no nosso plano proporcional com a influencia
        que o mundo oferece ao agente, em que caso se altera, o agente precisa alterar o seu plano.
        Seguidamente a condição, gera uma ação executada pelo operador

        Args:
            percepcao (Percepcao): contém a percepção do mundo ao agente

        Returns:
            Accao: processa uma ação
        """
        self.assimilar(percepcao)
        if (self.reconsiderar()):
            self.deliberar()
            self.planear()
        self.mostrar()
        return self.executar()

    def assimilar(self, percepcao):
        """
        O metodo informa sobre o mundo exterior ao agente, usando a percepção como os sensores/sentidos
        do agente

        Args:
            percepcao (Percepcao): sensor/sentido
        """
        self.__modelo_mundo.actualizar(percepcao)

    def reconsiderar(self):
        """
        Returns:
            bool: uma flag onde verifica se não há um plano ou se houve alteração no mundo
        """
        return not self.__plano or self.__modelo_mundo.alternado

    def deliberar(self):
        """
        cria/atualiza os objetivos fornecidos pelo mundo
        """
        self.__objetivos = self.__controlo.deliberar()

    def planear(self):
        """
        cria um plano usando o planeador que tem em conta o mundo inserido e os objetivos presentes no mundo

        o modelo mundo pode ser parametro do planeador porque este estende de ModeloPlan
        """
        self.__plano = self.__planeador.planear(
            self.__modelo_mundo, self.__objetivos)

    def executar(self):
        """
        cria um operador o qual será o operador passo da posição (estado) atual,
        com este operador, se existir, retunermos a ação (uma direção no caso) asssociada a este,
        se não houver o operador, o plano é descartado, logo isso será um trabalho para o metood reconsiderar

        Erro na semana 10, onde faltava o descarte do plano, corrigido no dia 16 de maio


        Returns:
            Accao: accao associada ao operador
        """
        if self.__plano:
            operador = self.__plano.obter_accao(
                self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao
            else:
                self.__plano = None

    def mostrar(self):
        self.vista.limpar()
        if self.__plano:
            self.__plano.mostrar(self.vista)
        self.__modelo_mundo.mostrar(self.vista)
        if self.__objetivos:
            for objetivo in self.__objetivos:
                self.vista.marcar_posicao(objetivo.posicao)
