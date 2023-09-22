package entities;

public class Camisa extends Roupa {

    public Camisa() {
    }

    public Camisa(String tamanho, String cor) {
        super(tamanho, cor);
    }

    public Camisa(String nome, String marca, String tamanho, String cor, double preco) {
        super(nome, marca, tamanho, cor, preco);
    }

    public double calcularPrecoFinal() {
        return super.preco * 0.9;
    }
}
