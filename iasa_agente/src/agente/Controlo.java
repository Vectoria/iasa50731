package agente;

public interface Controlo {
    //a interface controlo serve para processar uma ação, que para isso, primeiro precisa de uma percepção antes de acontecer
    public Accao processar(Percepcao percepcao);
}
