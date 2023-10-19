package entities;

public abstract class Correntista {
    protected double saldo;

    public Correntista(double saldo) {
        this.saldo = saldo;
    }

    public void debitar(double valor) {
        saldo = saldo - valor;
    }

    public void depositar(double valor) {
        saldo = saldo + valor;
    }

    public String toString() {
        return "Correntista\n" +
                "O saldo total é de: " + saldo;
    }
}
