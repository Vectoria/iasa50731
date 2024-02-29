package ambiente;

//pode ser para algo físico ou virtual
//possuí dependencia do Evento e Comando
// é associado para o Agente
// e é implementado no AmbienteJogo
public interface Ambiente {

    //no ambiente existem 3 acontecimentos: evoluir, observar e executar (algum comando)
    public void evoluir();

    public Evento observar();

    public void executar(Comando comando);
}
