package entities;

public abstract class Heroi extends Personagem{
    public Heroi(){
    }

    public Heroi(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void correr() {
        if (vivo) {
            System.out.println("Heroi correndo");
        } else {
            System.out.println(getClass().getSimpleName() + " não pode executar mais funções, esta morto");
        }
    }

    @Override
    public void saltar() {
        if (vivo) {
            System.out.println("Heroi saltando");
        } else {
            System.out.println(getClass().getSimpleName() + " não pode executar mais funções, esta morto");
        }
    }
}
