package maqest;

import agente.Accao;

/*
baixa acoplação, devido as suas associações
 */
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

//ready only
    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    public Accao getAccao() {
        return accao;
    }
}
