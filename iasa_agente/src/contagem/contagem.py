from mod_prob.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

""" 
ficheiro que serve para ver se o programa funciona bem

segue o enunciado que o professsor deu no dia 18 de abril
"""
VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2]

# Definir o Problema
problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

# Iniciar mecanismo de procura

# mec_proc = ProcuraProfundidade()
mec_proc = ProcuraCustoUnif()

# Resolver Problema

solucao = mec_proc.procurar(problema)

# Mostrar a solução, mostrando a iteração dos passos
for passo in solucao:
    print(passo.estado, passo.operador.incremento)
