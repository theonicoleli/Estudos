package entities;

public class Goldfinger extends Terrorista implements Personificacao{
    private Heroi heroi;

    public Goldfinger(){
    }

    public Goldfinger(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void camuflar(int cor) {
        if (vivo) {
            System.out.println("Goldfinger se camuflando de cor: " + cor);
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }

    @Override
    public void personificar(Heroi heroi) {
        if (vivo) {
            System.out.println("Goldfinger se transformou em " + heroi.getClass().getSimpleName());
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }

    public void setHeroi(Heroi heroi) {
        if (vivo) {
            this.heroi = heroi;
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }
}
