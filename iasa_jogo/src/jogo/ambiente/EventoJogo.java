package jogo.ambiente;

import ambiente.Evento;

public enum EventoJogo implements Evento {
    //os tipos do Jogo
    SILENCIO,
    RUIDO,
    ANIMAL,
    FUGA,
    FOTOGRAFIA,
    TERMINAR;

    //classe vinda do Evento
    @Override
    public void mostrar() {
        //imprime o proprio Enum
        System.out.printf("Evento: %s\n", this);

    }

}
