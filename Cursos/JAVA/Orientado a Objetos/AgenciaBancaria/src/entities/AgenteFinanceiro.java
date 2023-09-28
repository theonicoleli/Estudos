package entities;

public abstract class AgenteFinanceiro implements ServicoPagamento{

    public void estornar(Lojista lojista, Consumidor consumidor, double valor) {
        lojista.debitar(valor);
        consumidor.depositar(valor);
    }

    public abstract void cobrar(Lojista lojista, Consumidor consumidor, double valor);
}
