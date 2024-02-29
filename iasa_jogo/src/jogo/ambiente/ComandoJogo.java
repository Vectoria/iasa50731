package jogo.ambiente;

import ambiente.Comando;

public enum ComandoJogo implements Comando {
    //os tipos
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    //metodo do Comando
    @Override
    public void mostrar() {
        //imprime o proprio Enum
        System.out.printf("Acção: %s\n", this);
    }
}
