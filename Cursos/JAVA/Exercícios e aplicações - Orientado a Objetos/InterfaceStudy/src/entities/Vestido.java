package entities;

public class Vestido extends Roupa{

    public Vestido() {
    }

    public Vestido(String tamanho, String cor) {
        super(tamanho, cor);
    }

    public Vestido(String nome, String marca, String tamanho, String cor, double preco) {
        super(nome, marca, tamanho, cor, preco);
    }

    public double calcularPrecoFinal() {
        return super.preco * 0.8;
    }
}
