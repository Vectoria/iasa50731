package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;


/*
possui uma composição de transição
 */
public class Estado {
    /*
    na aula da semana 3, o professor quis que, ao inves do nome ser publico
    passa a ser privado, devido a manipulação de dados
     */

    private String nome;
    private Map<Evento, Transicao> transicoes;

    public Estado(String nome) {
        this.nome = nome;
        transicoes = new HashMap<Evento, Transicao>();
    }


    /*

     */
    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /*
    delta, proximo estado, funcao de saida

    haverá uma fatorização, por existir dois metodos com o mesmo proposito,
    em que a fatorização consiste em implementar o metodo mais concreto (o que tem Accao
    como parametro), e depois, o metodo mais abragente chama o metodo mais concreto
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /*
    lamda e delta

    dependencia com Accao
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }


    public String getNome() {
        return nome;
    }
}
