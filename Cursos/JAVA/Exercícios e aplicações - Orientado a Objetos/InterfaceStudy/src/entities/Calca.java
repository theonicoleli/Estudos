package entities;

public class Calca extends Roupa{

    public Calca() {
    }

    public Calca(String tamanho, String cor) {
        super(tamanho, cor);
    }

    public Calca(String nome, String marca, String tamanho, String cor, double preco) {
        super(nome, marca, tamanho, cor, preco);
    }

    public double calcularPrecoFinal() {
        return super.preco * 0.85;
    }
}
