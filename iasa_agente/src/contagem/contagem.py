from mod_prob.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2]

# Definir o Problema
problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

# Iniciar mecanismo de procura

mec_proc = ProcuraProfundidade()

# Resolver Problema

solucao = mec_proc.procurar(problema)

# Mostrar a solução
for passo in solucao:
    print(passo.estado, passo.operador.incremento)
