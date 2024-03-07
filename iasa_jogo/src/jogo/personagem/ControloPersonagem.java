package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;

/*
 acontece uma delegação, onde tem uma factorização funcional,
 em que tem um baixo acoplamento, devido a este implementar a interface de Controlo
 é dependido pelo Personagem
 */
public class ControloPersonagem implements Controlo {

    public ControloPersonagem() {
    }

    /*
    possuí uma dependencia com a Accao e Percepcao
     */
    @Override
    public Accao processar(Percepcao percepcao) {
        return null;
    }

    private void mostrar(){
        //System.out.printf("Acção: %s\n", this);
    }
}
