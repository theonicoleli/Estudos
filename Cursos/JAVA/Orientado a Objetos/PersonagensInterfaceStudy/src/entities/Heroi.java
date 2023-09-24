package entities;

public abstract class Heroi extends Personagem{
    public Heroi(){
    }

    public Heroi(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void correr() {
        System.out.println("Heroi correndo");
    }

    @Override
    public void saltar() {
        System.out.println("Heroi saltando");
    }
}
