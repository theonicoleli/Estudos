package application;

import entities.*;

public class Program {
    public static void main(String[] args) {
        Banco itau = new Banco("Itau", 0.02);
        VISA visa = new VISA();
        Lojista americanas = new Lojista(10000, 'C');
        Lojista amazon = new Lojista(20000, 'A');
        Consumidor carmem = new Consumidor(500.00);
        Consumidor beatriz = new Consumidor(800.00);

        ServicoPagamento servico;

        servico = itau;
        servico.cobrar(americanas, carmem, 200.00);
        System.out.println(carmem.toString());
        System.out.println(americanas.toString());

        System.out.println();

        servico.estornar(amazon, beatriz,100.00);
        System.out.println(amazon.toString());
        System.out.println(beatriz.toString());

        System.out.println();

        servico = visa;
        servico.cobrar(amazon, carmem, 300.00);
        System.out.println(carmem.toString());
        System.out.println(amazon.toString());

        System.out.println();

        servico.estornar(amazon, carmem, 50.00);
        System.out.println(carmem.toString());
        System.out.println(amazon.toString());
    }
}