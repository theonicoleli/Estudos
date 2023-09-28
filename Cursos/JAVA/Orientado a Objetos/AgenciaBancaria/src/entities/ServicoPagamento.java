package entities;

public interface ServicoPagamento {
    void cobrar(Lojista lojista, Consumidor consumidor, double valor);
    void estornar(Lojista lojista, Consumidor consumidor, double valor);
}
