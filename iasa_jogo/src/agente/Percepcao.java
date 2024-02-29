package agente;

import ambiente.Evento;

public class Percepcao {

    //existe o atributo evento, que é uma associação, onde a sua visibilidade é privada
    private Evento evento;

    public Percepcao(Evento evento) {
        this.evento = evento;
    }

    //este metodo existe de maneira que seja visivel publicamente, de maneira que o atributo evento seja "read only"
    public Evento getEvento() {
        return this.evento;
    }
}
