package entities;

public class Banco extends AgenteFinanceiro{
    private String nome;
    private double taxa;

    public Banco(){
    }

    public Banco(String nome, double taxa) {
        this.nome = nome;
        this.taxa = taxa;
    }

    @Override
    public void cobrar(Lojista lojista, Consumidor consumidor, double valor) {
        consumidor.debitar(valor);
        double tarifa = valor * taxa;
        lojista.depositar(valor - tarifa);
    }

}
