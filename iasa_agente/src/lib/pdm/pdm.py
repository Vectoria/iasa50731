from .mec_util import MecUtil


class PDM():
    """
    representa a propriedade de Markov
    """

    def __init__(self, modelo, gama, delta_max):
        """

        Instancia um mecanismo de utilidadee  passa o modelo no construtor.
        Na instanciação do mecanismo de utlidade, acontece a associação estrutural com o MecUtil

        Args:
            modelo (_type_): _description_
            gama (_type_): _description_
            delta_max (_type_): _description_
        """
        self.__mec_util = MecUtil(modelo, gama, delta_max)
        self.__modelo = modelo

    def politica(self, U):
        """
        É uma representação do comportamento do agente, na qual a ação que deve ser realizada
        em cada estado, definindo uma estratégia de ação.
        É derivado de utilidade
        -perguntar se é determinista ou n ???????????????????????????????????????????????????????????????

        Consiste em dado um conjunto de ações de um estado, guarda a ação de maior valor no dicionario

        Args:
            U (Utilidade): associação para escolher a ação num estado

        Returns:
            Politica: retorna a politica
        """
        S, A = self.__modelo.S, self.__modelo.A
        pol = {}
        for s in S():
            if A(s):
                pol[s] = max(
                    A(s), key=lambda a: self.__mec_util.util_accao(s, a, U)
                )
        return pol

    def resolver(self):
        """
        Consiste na utilidade de estado para uma política ótima pi

        Returns:
            Utilidade, Politica: _description_
        """
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U, pol
