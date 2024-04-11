class No:

    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        """ são 2 construtores, um que aceita so estado (para isso, existe um default noutros parametros), 
        e o outro que tem o estado, operdor, antecessor e custo

        caso haja antecessor, incrementamos a profundidade

        Args:
            estado (_type_): _description_
            operador (_type_, optional): _description_. Defaults to None.
            antecessor (_type_, optional): _description_. Defaults to None.
            custo (int, optional): _description_. Defaults to 0.
        """
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo

        if antecessor:

            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def custo(self):
        return self.__custo

    @property
    def estado(self):
        return self.__estado

    @property
    def operador(self):
        return self.__operador

    @property
    def antecessor(self):
        return self.__antecessor

    def __lt__(self, other):
        """
        compara a classe no atual com outra

        Args:
            other (No): _description_

        Returns:
            bool: 
        """
        return self.custo < other.custo
