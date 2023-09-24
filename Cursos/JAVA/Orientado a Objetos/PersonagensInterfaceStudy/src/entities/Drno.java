package entities;

public class Drno extends Terrorista{
    public Drno(){
    }

    public Drno(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void saltar() {
        System.out.println("Drno saltando");
    }

    @Override
    public void atirar() {
        System.out.println("Drno atirando");
    }

    @Override
    public void correr() {
        System.out.println("Drno correndo");
    }
}
