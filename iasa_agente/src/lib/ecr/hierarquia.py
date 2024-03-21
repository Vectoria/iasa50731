from .comport_comp import ComportComp

class Hierarquia(ComportComp):
    """
    A hierarquia é uma prioridade fixa

    Args:
        ComportComp (ComportComp): extende, por ser um mecanismo de combinação e seleção de ação de prioridade
    """    
    def selecionar_accao(self, accoes):
        """
        Por uma questão de simplicidade, a ação selecionada é a primeira da hierarquia

        Args:
            accoes (_type_): _description_

        Returns:
            Accao: _description_
        """        
        if accoes: 
            accao_sel = accoes[0]
            return accao_sel