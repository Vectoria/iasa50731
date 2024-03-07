package jogo.ambiente;

import ambiente.Evento;

/*
é usando tanto para a composição quanto para associação do AmbienteJogo
delegação, onde tem factorização funcional, por implementar o Evento
*/

public enum EventoJogo implements Evento {
    //os tipos de Eventos que existem
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
