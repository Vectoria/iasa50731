package jogo.ambiente;

import ambiente.Comando;

public enum ComandoJogo implements Comando {
    //os tipos de Comandos existentes
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    @Override
    public void mostrar() {
        //imprime o proprio Enum
        System.out.printf("Acção: %s\n", this);
    }
}
