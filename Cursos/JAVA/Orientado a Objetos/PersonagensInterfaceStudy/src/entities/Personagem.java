package entities;

public abstract class Personagem implements AtividadesPersonagem{

    private boolean vivo;
    private double posicao_x;
    private double posicao_y;
    private double posicao_z;
    private int cor;

    public Personagem(){
    }

    public Personagem(boolean vivo, double posicao_x, double posicao_y, double posicao_z, int cor) {
        this.vivo = vivo;
        this.posicao_x = posicao_x;
        this.posicao_y = posicao_y;
        this.posicao_z = posicao_z;
        this.cor = cor;
    }

    public void correr(){
        System.out.println("Correndo");
    }

    public void saltar(){
        System.out.println("Saltando");
    }

    public void atirar() {
        System.out.println("Atirando");
    }

    public void morrer() {
        vivo = false;
    }

    public boolean getVivo(){
        return vivo;
    }

    public void vivoMorto() {
        if (vivo) {
            System.out.println( getClass().getSimpleName() + " está vivo!");
        } else {
            System.out.println( getClass().getSimpleName() + " está morto.");
        }
    }
}
