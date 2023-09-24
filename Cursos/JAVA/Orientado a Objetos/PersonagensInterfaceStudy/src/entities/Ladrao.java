package entities;

public abstract class Ladrao extends Vilao{
    public Ladrao(){
    }

    public Ladrao(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void saltar() {
        System.out.println("Ladrão saltando");
    }
}
