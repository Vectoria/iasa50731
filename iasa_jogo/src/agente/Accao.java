package agente;

import ambiente.Comando;

// é dependente do Controlo, ControloPersonagem
public class Accao {

    //existe o atributo comando, que é uma associação, onde a sua visibilidade é privada
    private Comando comando;

    public Accao(Comando comando) {
        this.comando = comando;
    }

    //este metodo existe de maneira que seja visivel publicamente, de maneira que o atributo comando seja "read only"
    public Comando getComando() {
        return comando;
    }
}
