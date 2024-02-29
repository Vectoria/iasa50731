package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.ArrayList;
import java.util.List;

public class AmbienteJogo implements Ambiente {
    private EventoJogo evento;
    //private Evento[] eventos= new Evento[10];
    private List<Evento> eventos = new ArrayList<Evento>();
    private ComandoJogo comandoJogo;

    public AmbienteJogo() {
    }

    @Override
    public void evoluir() {

    }

    @Override
    public Evento observar() {
        comandoJogo = ComandoJogo.OBSERVAR;
        return null;
    }

    @Override
    public void executar(Comando comando) {

    }

    public EventoJogo gerarEvento() {
        //switch case do comando para gerar evento?
        return null;
    }

    public EventoJogo getEventoJogo() {
        return evento;
    }
}
