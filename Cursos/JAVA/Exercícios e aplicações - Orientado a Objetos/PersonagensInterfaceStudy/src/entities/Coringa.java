package entities;

public class Coringa extends Ladrao{
    public Coringa(){
    }

    public Coringa(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    public void atirar() {
        if (vivo) {
            System.out.println("Coringa atirando");
        } else {
            System.out.println(getClass().getSimpleName() + " não pode executar mais funções, esta morto");
        }
    }
}
