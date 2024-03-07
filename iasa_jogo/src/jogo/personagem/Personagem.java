package jogo.personagem;

import agente.Accao;
import agente.Agente;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Ambiente;
import ambiente.Evento;

/*
 possuí um forte acoplamento devido ao Personagem extender do Agente
 também acontece a fatorização estrutural, pelo mesmo motivo
 também possuí uma otima coesão por ter bem as partes agrupadas (como
 o extentimento do Agente, dependencia com o Ambiente e ControloPersonagem)
 slide

 é concreto, em que é focagem da abstração do agente, em que tem mais complexidade

 */
public class Personagem extends Agente {
    public Personagem(Ambiente ambiente) {
        //dependencia com o ControloPersonagem e ambiente
        super(ambiente, new ControloPersonagem());
    }

    @Override
    public void executar() {
        super.executar();
    }

    @Override
    protected Percepcao percepcionar() {


        return super.percepcionar();
    }

    @Override
    protected void actuar(Accao accao) {
        super.actuar(accao);
    }


}
