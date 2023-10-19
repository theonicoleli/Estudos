package entities;

public class Consumidor extends Correntista{
    private int pontos;


    public Consumidor(double saldo) {
        super(saldo);
        pontos = 0;
    }

    public void bonificar(int pontos){
        this.pontos = this.pontos + pontos;
    }
}
