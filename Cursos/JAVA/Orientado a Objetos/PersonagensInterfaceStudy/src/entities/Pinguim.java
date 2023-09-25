package entities;

public class Pinguim extends Ladrao{
    public Pinguim(){
    }

    public Pinguim(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void atirar() {
        if (vivo) {
            System.out.println("Pinguim atirando");
        } else {
            System.out.println(getClass().getSimpleName() + " não pode executar mais funções, esta morto");
        }
    }

    @Override
    public void correr() {
        if (vivo) {
            System.out.println("Pinguim correndo");
        } else {
            System.out.println(getClass().getSimpleName() + " não pode executar mais funções, esta morto");
        }
    }
}
