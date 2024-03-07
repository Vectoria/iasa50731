package agente;

import ambiente.Ambiente;
import ambiente.Evento;
import jogo.personagem.Personagem;

/*
possuí o Ambiente, e tem composição do Controlo
é extende o Personagem
alto acoplamento por ter composição
também possui uma alta abstração, com menor complexidade
*/
public class Agente {
    //os variaveis correspondem a associação do ambiente ao agente, e a composição do controlo ao agente
    private Ambiente ambiente;
    private Controlo controlo;

    //inicialização destas variaveis
    //injeção de dependencias (com o controlo)
    public Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /*
    Pelo diagrama de atividades do slide 10 (onde foi convertido do modelo conceitual),
    possuímos duas swimlanes, agente e controlo.

    Também há um fluxo de objetos (sequencia de ativações), onde inici-se com
    o percepcionar do agente, que este será a declaração da percepcao
    de seguida usamos a percepção como parametro do processar do controlo
    com o processar do controlo, gera accao
    que no fim, a accao sera usada como parametro do actuar do agente
     */
    public void executar() {
        Percepcao percepcao = percepcionar();
        Accao accao = this.controlo.processar(percepcao);
        actuar(accao);
    }


    //classe responsável por fazer o agente ter uma percepção de algum evento
    protected Percepcao percepcionar() {
        /*
        como queremos um tipo "Percepcao" e apenas temos o ambiente e controlo,
        usamos o ambiente de maneira que da-nos um evento
        com o evento extraido, usamos este para criar o tipo "Percepcao"
        */
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
