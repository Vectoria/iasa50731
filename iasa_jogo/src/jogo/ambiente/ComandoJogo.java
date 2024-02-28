package jogo.ambiente;

import ambiente.Comando;

public enum ComandoJogo implements Comando {
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    @Override
    public void mostrar() {
        //ig
        for (ComandoJogo comandoJogo : ComandoJogo.values()) {
            System.out.println(comandoJogo);
        }
    }
}
