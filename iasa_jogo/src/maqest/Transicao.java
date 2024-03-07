package maqest;

import agente.Accao;

public class Transicao {
    /*
    associação com o Estado e Accao
     */
    private Estado estadoSucessor;
    private Accao accao;


    public Transicao(Estado estadoSucessor, Accao accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }


    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    public Accao getAccao() {
        return accao;
    }
}
