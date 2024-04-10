package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/*
 contem composição do AmbienteJogo e Personagem
 alto acoplamento devido a composição

 Também nele é aplicado o modelo de interação
 */
public class Jogo {
    private static Personagem personagem;
    private static AmbienteJogo ambienteJogo;

    /*
    declaração do ambiente do Jogo e personagem, e de seguida o executar,
    como esta presente no diagrama de sequencia
     */
    public static void main(String[] args) {
        ambienteJogo = new AmbienteJogo();
        personagem = new Personagem(ambienteJogo);
        executar();
    }


    /*
    Como esta presente no diagrama de sequencia
    onde contém um loop, no caso, do-while (a preferencia deste loop dá-se pelo facto que
    precisamos primeiro evoluir o ambienteJogo antes de verificamos que o evento seja terminado)

    na aula, o professor queria que o metódo fosse privado

    aqui tinha um erro que ao inves de por "!=", punha .equals, em que travava o jogo
     */
    private static void executar() {
        do {
            ambienteJogo.evoluir();
            personagem.executar();
        } while (ambienteJogo.getEvento() != EventoJogo.TERMINAR);

    }
}
