package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.*;

//encapsulamento por causa do Ambiente
public class AmbienteJogo implements Ambiente {
    private Scanner scanner= new Scanner(System.in);
    private EventoJogo evento;
    private Map<String, EventoJogo> eventos; //comportamento
    private ComandoJogo comandoJogo;

    //iniciar o map
    public AmbienteJogo() {
        eventos= new HashMap<String,EventoJogo>();

        //cada letra corresponde a uma
        eventos.put("s",EventoJogo.SILENCIO);
        eventos.put("r",EventoJogo.RUIDO);
        eventos.put("a",EventoJogo.ANIMAL);
        eventos.put("f",EventoJogo.FUGA);
        eventos.put("o",EventoJogo.FUGA);
        eventos.put("t",EventoJogo.TERMINAR);

    }

    //atualiza o evento usando o gerarEvento
    @Override
    public void evoluir() {
        evento = gerarEvento();
    }

    @Override
    public Evento observar() {
        //comandoJogo = ComandoJogo.OBSERVAR;
        evento.mostrar();
        return evento;
    }

    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    //s silencio
    //r ruido
    // a animal presente
    //f fuga
    //t terminar
    //o terminar
    public EventoJogo gerarEvento() {
        //switch case do comando para gerar evento?
        System.out.println("Qual evento queres?");
        String comando= scanner.next();
        return eventos.get(comando);
    }

    public EventoJogo getEventoJogo() {
        return evento;
    }
}
