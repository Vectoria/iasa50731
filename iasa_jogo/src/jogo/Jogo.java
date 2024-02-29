package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

public class Jogo {
    private static Personagem personagem;
    private static AmbienteJogo ambienteJogo;

    public static void main(String[] args) {
        ambienteJogo = new AmbienteJogo();
        personagem = new Personagem();
        executar();
    }

    //na aula queria em privado
    private static void executar() {
        do {
            ambienteJogo.evoluir();
         //   personagem.executar();
        } while (!ambienteJogo.getEventoJogo().equals(EventoJogo.TERMINAR));

    }
}
