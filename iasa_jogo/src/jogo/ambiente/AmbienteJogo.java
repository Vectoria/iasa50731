package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

public class AmbienteJogo implements Ambiente {
    private EventoJogo evento;
    private Evento[] eventos= new Evento[10];
    private ComandoJogo comandoJogo;

    public AmbienteJogo() {
    }

    @Override
    public void evoluir() {

    }

    @Override
    public Evento observar() {
        comandoJogo= ComandoJogo.OBSERVAR;
        return null;
    }

    @Override
    public void executar(Comando comando) {

    }

    public EventoJogo gerarEvento(){

        return null;
    }

    public EventoJogo getEventoJogo() {
        return evento;
    }
}
