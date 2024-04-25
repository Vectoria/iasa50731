from .passo_solucao import PassoSolucao


class Solucao:
    """
    Possuí uma acoplaçãopo média por ter agregação

    Classe que mostra a solução do problema, quando antinge o objetivo, em que mostra
    o percurso no espaço de estados, ou seja, entre o estado inicial até ao estado objetivo 
    existem uma sequência de estados e operadores
    """

    def __init__(self, no_final):
        """
        Capta o nó final e mostra o percurso, atráves de profundidade, até chegar ao nó inicial (que este não possuí antecessor)
        Para o percurso, apenas cria-se uma varivale que guarda o tuplo devolvido pela classe "PassoSolução", que no caso é o estado anterior
        e o operador, e guarda tal passo numa lista

        Args:
            no_final (No): Como o nome indica, é o nó da solução do problema
        """
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo)
            no = no.antecessor

    @property
    def dimensao(self):
        """profundidade da solução, ou seja, quantos estados houveram do estado inicial até ao estado da solução
        """
        return self.__no_final.profundidade

    @property
    def custo(self):
        """retorna o custo total da solução
        """
        return self.__no_final.custo

    def __iter__(self):
        """faz como que a lista de passos torna iterativa para um ciclo for
        """
        return iter(self.__passos)

    def __getitem__(self, index):
        """ quando usa um nº nos parenteses retos a um item do tipo desta classe, devolve nº do passo na lista de passos
        """
        return self.__passos[index]
