package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;


/*
possui uma composição de transição
devido a isso, alto acoplamento
 */
public class Estado {
    /*
    na aula da semana 3, o professor quis que, ao inves do nome ser publico
    passa a ser privado, devido a manipulação de dados ser mais versatil
     */

    private String nome;
    private Map<Evento, Transicao> transicoes;

    public Estado(String nome) {
        this.nome = nome;
        transicoes = new HashMap<Evento, Transicao>();
    }


    /*
    diagrama de sequencias, onde o processar usa o Hashmap, introduzindo um evento, para ver qual será
    a Transição
     */
    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /*
    lamda, função de transição, onde tem o simbolo da entrada

    Modelo Mealy
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /*
    haverá uma fatorização, por existir dois metodos com o mesmo proposito,
    em que a fatorização consiste em implementar o metodo mais concreto (o que tem Accao
    como parametro), e depois, o metodo mais abragente chama o metodo mais concreto

    lamda e delta, ou seja, função de transição de estaod e função de saída,
    em que o primeiro é simbolo da entrada e o segundo é saída

    Modelo Mealy
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }


    public String getNome() {
        return nome;
    }
}
