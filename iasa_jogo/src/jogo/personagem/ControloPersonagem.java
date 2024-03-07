package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

import static jogo.ambiente.ComandoJogo.PROCURAR;

/*
 acontece uma delegação, onde tem uma factorização funcional,
 em que tem um baixo acoplamento, devido a este implementar a interface de Controlo
 é dependido pelo Personagem
 */
public class ControloPersonagem implements Controlo {
    //composição da MaquinaEstados
    private MaquinaEstados maquinaEstados;


    /*
    atráves do diagrama de transição de estado, slide 13,
    fazemos a definição de comportamento do personagem e as suas transições
    A maquina de estados inicia-se com a procura, como esta no diagrama

    encadiamento de instruções, sendo mais pratico (isso se deve ao return this, na
    implementação do metodo)
     */
    public ControloPersonagem() {
        Estado procura = new Estado("Procura");
        Estado inspeccao = new Estado("Inspecção");
        Estado observacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        Accao procurar= new Accao(ComandoJogo.PROCURAR);
        Accao aproximar= new Accao(ComandoJogo.APROXIMAR);
        Accao observar= new Accao(ComandoJogo.OBSERVAR);
        Accao fotografar= new Accao(ComandoJogo.FOTOGRAFAR);

        procura
                .transicao(EventoJogo.RUIDO,inspeccao,aproximar)
                .transicao(EventoJogo.ANIMAL,observacao,aproximar)
                .transicao(EventoJogo.SILENCIO,procura,procurar);

        inspeccao
                .transicao(EventoJogo.ANIMAL,observacao,aproximar)
                .transicao(EventoJogo.SILENCIO,procura)
                .transicao(EventoJogo.RUIDO,inspeccao,procurar);

        observacao
                .transicao(EventoJogo.ANIMAL,registo,observar)
                .transicao(EventoJogo.FUGA,inspeccao);

        registo
                .transicao(EventoJogo.ANIMAL,registo,fotografar)
                .transicao(EventoJogo.FUGA,procura)
                .transicao(EventoJogo.FOTOGRAFIA,procura);

        maquinaEstados= new MaquinaEstados(procura);
    }

    /*
    Possuí uma dependencia com a Accao e Percepcao
    Obedece ao diagrama de sequencias, slide 15,
    também acontece delegação, por causa da maquina de estados
     */

    @Override
    public Accao processar(Percepcao percepcao) {
        Evento evento= percepcao.getEvento();
        Accao accao= maquinaEstados.processar(evento);
        mostrar();
        return accao;
    }

    //print do nome do estado
    private void mostrar() {
        System.out.printf("Estado: %s\n", getEstado().getNome());
    }

    //associação com o Estado
    //factorização funcional, delegação
    public Estado getEstado() {
        return maquinaEstados.getEstadoInicial();
    }
}
