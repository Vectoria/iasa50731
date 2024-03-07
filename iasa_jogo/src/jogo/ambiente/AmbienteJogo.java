package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.*;

/*
 encapsulamento baixo por causa do Ambiente, por implementar este
 possui uma dependencia do ComandoJogo
 é composto pelo Jogo
 Factorização funcional, delegação
 */

public class AmbienteJogo implements Ambiente {
    private Scanner scanner = new Scanner(System.in);
    //assoicação do EventoJogo
    private EventoJogo evento;
    //composição do EventoJogo
    private Map<String, EventoJogo> eventos; //comportamento


    //a função do construtor é iniciar o Map
    public AmbienteJogo() {
        eventos = new HashMap<String, EventoJogo>();

        //é armazenado todos os eventos, juntamente com cada respectiva letra, no hasmap
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);

    }

    //atualiza o evento gerando um evento (usando a declaração do gerarEvento)
    @Override
    public void evoluir() {
        evento = gerarEvento();
    }

    //serve para dar uma print relativamente ao evento
    @Override
    public Evento observar() {
        evento.mostrar();
        return evento;
    }

    //serve para dar uma print relativamente ao comando
    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    //pede ao utilizador para clicar numa letra para gerar um Evento
    public EventoJogo gerarEvento() {
        System.out.println("Qual evento queres?");
        String comando = scanner.next();
        //com a letra clicada, procura a assoicação desta letra a um evento dentro do HashMap
        return eventos.get(comando);
    }
    /*
     na aula houve o pensamento de usar um switch case ao invés de um HashMap, mas devido ao
     Hashmap manipular diretamente a estrutura de dados, então preferiu-se este (estrutura associativa de dados)
     */


    public EventoJogo getEvento() {
        return evento;
    }
}
