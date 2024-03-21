from .comport_comp import ComportComp

class Prioridade(ComportComp):
    def selecionar_accao(self, accoes):
        """
        o max é uma função que não necessida de estrutura interna para devolver o maior número, dentro do array
        por accoes serem do objeto "Accao", então deverá ser necessario uma key para definir 
        que número queremos comparar, para tal é usado uma função lambda (função anónima),
        que será a função com a entrada de accaoe retorna o número de prioridade da ação,
        em outras palavras, a função lambada será responsavel por devolver o valor da prioridade (um valor númerico), 
        desta forma é possível fazer o max das accoes e escolher o que tem o maior valor de prioridade

        Args:
            accoes (Accao): lista de ações existentes, em que cada uma tem sua prioridade
        """        
        if accoes:
            accao_sel= max(accoes, key= lambda accao: accao.prioridade)
            return accao_sel