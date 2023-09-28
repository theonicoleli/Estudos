package entities;

public class VISA extends AgenteFinanceiro{
    @Override
    public void cobrar(Lojista lojista, Consumidor consumidor, double valor) {
        consumidor.debitar(valor);
        consumidor.bonificar( (int) (valor/100));
        double taxa = 0.05;
        if (lojista.categoria() == 'A') {
            taxa = 0.02;
        } else if (lojista.categoria() == 'B') {
            taxa = 0.07;
        }
        double tarifa = valor * taxa;
        lojista.depositar(valor - tarifa);
    }
}
