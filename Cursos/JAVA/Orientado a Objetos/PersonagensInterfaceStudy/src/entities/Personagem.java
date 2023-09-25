package entities;

public abstract class Personagem implements AtividadesPersonagem{

    protected boolean vivo;
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
        if (vivo) {
            System.out.println("Correndo");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }

    public void saltar(){
        if (vivo) {
            System.out.println("Saltando");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }

    public void atirar() {
        if (vivo) {
            System.out.println("Atirando");
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
    }

    public void morrer() {
        if (vivo) {
            vivo = false;
        } else {
            System.out.println(getClass().getSimpleName() + " está morto");
        }
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
