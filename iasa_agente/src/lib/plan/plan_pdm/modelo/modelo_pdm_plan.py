from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan


class ModeloPDMPlan(ModeloPDM, ModeloPlan):
    """
    Classe que representa o modelo plano das propriedade de Markov definido

    Ao longo da classe, os meotdos obter_estado, obter_estados e obter_operadores, poussem
    delegação

    Args:
        ModeloPDM (ModeloPDM): implementa a interface
        ModeloPlan (ModeloPlan): implementa a interface
    """

    def __init__(self, modelo_plan, objetivos, rmax=1000):
        """

        Args:
            modelo_plan (ModeloPlan): palno do modelo onde será usado fatorização
            objetivos (list): lista dos objetivos
            rmax (int, optional): É a recompensa maxima, podendo ser perda ou ganho (ao antigir o alvo). Defaults to 1000.
        """
        self.__modelo_plan = modelo_plan
        self.__objetivos = objetivos
        self.__rmax = rmax
        self.__transicoes = {(s, a): a.aplicar(s)
                             for s in self.obter_estados()
                             for a in self.obter_operadores()}

    def obter_estado(self):
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        return self.__modelo_plan.obter_estados()

    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    def S(self):
        return self.obter_estados()

    def A(self, s):
        """
        Erro na semana 12, onde caso não cumprisse a condição, retornava um dicionario vazio,
        ao ínves de uma lista, apesar que o programa executa normalmente, é um erro por não
        seguir o UML, corrigido no dia 16 de abril

        Args:
            s (Estado): estado inserido

        Returns:
            lista de Operadores: devolve a lista de operadores se o não estado existir nos objetivos
        """
        return self.obter_operadores() if s not in self.__objetivos else []

    def T(self, s, a, sn):
        """
         probabilidade de transição de s para s' através de a, em estados deterministicos

        Args:
            s (Estado): estado atual
            a (Operador): operador do estado atual para o seguinte
            sn (Estado): estado seguinte

        Returns:
            double: a probabilidade da transição
        """
        # return 1 if self.suc(s, a) else 0 #forma menos eficaz, que não usa o estado seguinte

        # forma mais eficaz
        return 1 if self.__transicoes.get((s, a)) == sn else 0

    def R(self, s, a, sn):
        """
        recompensa esperada na transição de s para s' através de a, onde se 
        tiver o estado sucessor nos objetivos, é um ganho, se não tiver, terá
        uma perda (recompensa negativa) calculada pelo custo do estado para estado seguinte

        Args:
            s (Estado): estado atual
            a (Operador): operador do estado atual para o seguinte
            sn (Estado): estado seguinte

        Returns:
            double: probabilidade da recompensa
        """
        return self.__rmax if sn in self.__objetivos else -a.custo(s, sn)

    def suc(self, s, a):
        """
        Sucessao de um estado usando um operador

        Args:
            s (Estado): estado atual
            a (Operador): operador do estado atual para o seguinte

        Returns:
            lista de Estados: devolve a transição que esta atrelado ao estado atual e
            a açã, se existir
        """
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []
