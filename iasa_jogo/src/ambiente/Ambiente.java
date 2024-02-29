package ambiente;

//pode ser para algo físico ou virtual
public interface Ambiente {

    //no ambiente existem 3 acontecimentos: evoluir, observar e executar (algum comando, podendo ser uma ação)
    public void evoluir();

    public Evento observar();

    public void executar(Comando comando);
}
