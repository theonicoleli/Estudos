public class Carros {
    private final int id;
    private final String modelo;
    private final String cor;
    private final int ano;
    private double valor;

    public Carros(int id, String modelo, String cor, int ano, double valor) {
        this.id = id;
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
        this.valor = valor;
    }

    public void setNewValor(double newValor) {
        this.valor = newValor;
    }

    public double getValor() {
        return this.valor;
    }

    public int getId() {
        return this.id;
    }

    public void showCar() {
        System.out.printf("O id do carro é: %d\n" +
                "Seu modelo é: %s\n" +
                "Sua cor é: %s\n" +
                "Seu ano é: %d\n" +
                "Seu valor é: %.2f",
                this.id,
                this.modelo,
                this.cor, this.ano,
                this.valor
                );
    }
}