package entities;

public class Drno extends Terrorista{
    public Drno(){
    }

    public Drno(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void saltar() {
        if (vivo) {
            System.out.println("Drno saltando");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }

    @Override
    public void atirar() {
        if (vivo) {
            System.out.println("Drno atirando");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }

    @Override
    public void correr() {
        if (vivo) {
            System.out.println("Drno correndo");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }
}
