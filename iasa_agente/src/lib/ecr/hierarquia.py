from .comport_comp import ComportComp

class Hierarquia(ComportComp):
    """
    A hierarquia é uma prioridade fixa, ou seja, não varia com o tempo ou com o ambiente,
    que cada sub-comportamento tem a sua prioridade imutavel

    Acoplamento alto, por haver extend

    Args:
        ComportComp (ComportComp): extende, por ser um mecanismo de combinação e seleção de ação de prioridade
    """    
    def selecionar_accao(self, accoes):
        """
        Por uma questão de simplicidade da hierarquia, a ação selecionada é a primeira da lista,
        as outras ações sofrem de subsução, ou seja, podem ser suprimidas e substituidas pelas ações
        que estão primeiro na lista

        Args:
            accoes (Accao): lista de ações, em que o primeiro tem mais prioridade

        Returns:
            Accao: retorna a primeira ação, o que tem mais prioridade
        """        
        if accoes: 
            accao_sel = accoes[0]
            return accao_sel