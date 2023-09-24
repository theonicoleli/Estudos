package entities;

public class Pinguim extends Ladrao{
    public Pinguim(){
    }

    public Pinguim(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void atirar() {
        System.out.println("Pinguim atirando");
    }

    @Override
    public void correr() {
        System.out.println("Pinguim correndo");
    }
}
