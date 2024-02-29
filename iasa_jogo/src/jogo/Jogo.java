package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

//contem composição do AmbienteJogo e Personagem
// alto acoplamento
public class Jogo {
    private static Personagem personagem;
    private static AmbienteJogo ambienteJogo;

    public static void main(String[] args) {
        ambienteJogo = new AmbienteJogo();
        personagem = new Personagem(ambienteJogo);
        executar();
    }

    //na aula queria em privado
    private static void executar() {
        do {
            ambienteJogo.evoluir();
         //   personagem.executar();
        } while (!ambienteJogo.getEvento().equals(EventoJogo.TERMINAR));

    }
}
