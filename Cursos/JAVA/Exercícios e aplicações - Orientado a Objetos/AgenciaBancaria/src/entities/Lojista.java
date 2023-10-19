package entities;

public class Lojista extends Correntista{
    private char categoria;

    public Lojista(double saldo, char categoria) {
        super(saldo);
        this.categoria = categoria;
    }

    public char categoria() {
        return categoria;
    }

    public String toString() {
        return "LOJISTA\n" +
                "O saldo total é de: " + saldo + "\nE a categória é: " + categoria;
    }
}
