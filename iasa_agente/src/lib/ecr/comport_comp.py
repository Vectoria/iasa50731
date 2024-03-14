from .comportamento import Comportamento

class ComportComp(Comportamento):
    def __init__(self, comportamentos):
        self.__comportamentos=comportamentos


    def activar(self, percepcao):
        """
        ãtivação do comportamento composto, onde percorremos todos os comportamentos existentes
        em que cria varias ações atraves de uma percepção, depois de criar as demais ações, acontece a 
        escolha da ação ideal 

        Args:
            percepcao (Percepcao): _description_

        Returns:
            Accao: _description_
        """        
        accoes=[]
        for comp in self.__comportamentos:
            accao=comp.activar(percepcao)
            if accao is not None:
                accoes.append(accao)
        if accoes is not None:
            return self.selecionar_accao(accoes)
    
    
    @Comportamento.__abstractmethods__
    def selecionar_accao(self,accoes):
        """delegação, factorização funcional para o metodo ser abstracto

        Args:
            accoes (_type_): _description_
        """        
        "Accao"