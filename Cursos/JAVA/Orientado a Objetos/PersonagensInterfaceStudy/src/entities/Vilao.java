package entities;

public abstract class Vilao extends Personagem{
    public Vilao(){
    }

    public Vilao(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void correr() {
        if (vivo) {
            System.out.println("Vilão correndo");
        } else {
            System.out.println(getClass().getSimpleName() + " não pode executar mais funções, esta morto");
        }
    }
}
