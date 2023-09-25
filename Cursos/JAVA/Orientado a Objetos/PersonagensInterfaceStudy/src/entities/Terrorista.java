package entities;

public abstract class Terrorista extends Vilao{
    public Terrorista(){
    }

    public Terrorista(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void atirar() {
        if (vivo) {
            System.out.println("Terrorista atirando");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }
}
