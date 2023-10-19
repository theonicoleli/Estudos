package entities;

public abstract class Roupa implements Produto{

    private String nome;
    private String marca;
    protected double preco;
    private String tamanho;
    private String cor;

    public Roupa(){
    }

    public Roupa(String tamanho, String cor) {
        this.tamanho = tamanho;
        this.cor = cor;
    }

    public Roupa(String nome, String marca, String tamanho, String cor, double preco) {
        this.nome = nome;
        this.marca = marca;
        this.tamanho = tamanho;
        this.preco = preco;
    }

    public String getTamanho() {
        return tamanho;
    }

    public void setTamanho(String tamanho) {
        this.tamanho = tamanho;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getNome() {
        return nome;
    }

    public String getMarca() {
        return marca;
    }

    public double getPreco(){
        return preco;
    }

    public void setPreco(double preco){
        this.preco = preco;
    }

    public String toString() {
        return "Cliente nome: " +
                this.nome +
                ", Marca: " +
                this.marca +
                ", Tamanho: " +
                this.marca +
                ", Cor: " +
                this.marca +
                ", Preço: " +
                String.format("%.2f", calcularPrecoFinal());
    }

    public abstract double calcularPrecoFinal();
}
