package maqest;

import agente.Accao;
import ambiente.Evento;

/*
possuí fraco acoplamento devido a associação
 */
public class MaquinaEstados {
    //associação com Estado
    private Estado estadoInicial;


    public MaquinaEstados(Estado estadoInicial) {
        this.estadoInicial = estadoInicial;
    }

    //dependencia com Accao
    /*
    aplicação de um diagrama de sequencias para a maquina de estado, presente no slide 11
    em que é criado uma Transição atraves do estado que tem nesta classe,
    que processa uma transição dependendo do evento do parametro
    caso a transição não seja vazia, o estado que temos passa para o seguinte e da return a ação

    delegação por causa do estadoInicial e transicao
     */
    public Accao processar(Evento evento) {

        Transicao transicao = estadoInicial.processar(evento);
        if (transicao != null) {
            estadoInicial = transicao.getEstadoSucessor();
            Accao accao = transicao.getAccao();
            return accao;
        } else {
            return null;
        }
    }

    //read only
    public Estado getEstadoInicial() {
        return estadoInicial;
    }
}
