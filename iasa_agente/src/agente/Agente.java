package agente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

public class Agente {
    //os variaveis correspondem a associação do ambiente ao agente, e a composição do controlo ao agente
    private Ambiente ambiente;
    private Controlo controlo;

    //inicialização destas variaveis
    public Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    public void executar() {

    }


    //classe responsável por fazer o agente ter uma percepção de algum evento
    protected Percepcao percepcionar() {
        //como queremos um tipo "Percepcao" e apenas temos o ambiente e controlo, usamos o ambiente de maneira que da-nos um evento
        //com o evento extraido, usamos este para criar o tipo "Percepcao"
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    //classe responsavel para o agente efetuar uma ação no ambiente
    protected void actuar(Accao accao) {
        //verificasse se a ação existe
        if (accao != null) {
            //com a ação, é possivel ter um comando
            //com o comando que pode ser encontrado na ação, deduzimos o uso da variável ambiente, juntamente
            // com a função que tem como parametro, o tipo Comando
            ambiente.executar(accao.getComando());
        }
    }


}
