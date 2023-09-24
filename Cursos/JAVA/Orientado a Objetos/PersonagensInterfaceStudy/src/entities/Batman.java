package entities;

public class Batman extends Heroi implements Camuflagem{
    public Batman() {
    }

    public Batman(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void atirar() {
        System.out.println("Batman atirando");
    }

    @Override
    public void camuflar(int cor) {
        System.out.println("Batman se camuflando de cor: " + cor);
    }
}
