from mod_prob.heuristica_contagem import HeuristicaContagem
from mod_prob.problema_contagem import ProblemaContagem
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

""" 
ficheiro que serve para ver se o programa funciona bem

segue o enunciado que o professsor deu no dia 18 de abril

no dia 2 de maio, o mecanismo de procura agora, pode ser escolhido uma procura de custo uniforme,
uma procura sofrega, uma procura A*
"""
VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2, -1]

# Definir o Problema
problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)
heuristica = HeuristicaContagem(VALOR_FINAL)

# Iniciar mecanismo de procura

# mec_proc = ProcuraProfundidade()
# mec_proc = ProcuraCustoUnif()
mec_proc = ProcuraAA()

# Resolver Problema

solucao = mec_proc.procurar(problema, heuristica)

# Mostrar a solução, mostrando a iteração dos passos
for passo in solucao:
    print(passo.estado, passo.operador.incremento)
