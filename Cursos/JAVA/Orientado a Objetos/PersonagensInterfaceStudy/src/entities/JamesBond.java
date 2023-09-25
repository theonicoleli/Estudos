package entities;

public class JamesBond extends Heroi{
    public JamesBond(){
    }

    public JamesBond(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void atirar() {
        if (vivo) {
            System.out.println("James Bond atirando");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }

    @Override
    public void saltar() {
        if (vivo) {
            System.out.println("James Bond saltando");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }
}
