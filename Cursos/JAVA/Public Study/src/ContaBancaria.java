import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;

public class ContaBancaria {
    private String nome;
    private int idade;
    private String numeroDaConta;
    private String CPF;
    private Double saldoDisponivel;

    public ContaBancaria(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu nome: ");
        this.nome = scanner.nextLine();
        System.out.println("Digite sua idade: ");
        this.idade = scanner.nextInt();
        System.out.println("Digite seu CPF: ");
        scanner.nextLine();
        this.CPF = scanner.nextLine();
        System.out.println("Digite o saldo disponível: ");
        this.saldoDisponivel = scanner.nextDouble();
    }

    public String numeroContaRandom() {
        ArrayList<Integer> lista = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 11; i++) {
            lista.add(random.nextInt(9));
        }
        String numeroDaConta = "";
        for (Integer n : lista) {
            numeroDaConta += n;
        }
        this.numeroDaConta = numeroDaConta;
        return this.numeroDaConta;
    }

    public void setNewMoney(Double newValor) {
        this.saldoDisponivel -= newValor;
    }

    public void setMoneyPlus(Double newValor) {
        this.saldoDisponivel += newValor;
    }

    public void retirarDinheiro(int op, String numeroDaConta) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Conta bancária: " + numeroDaConta);
        System.out.println("Seu saldo disponível é de: " + this.saldoDisponivel);
        if (op == 1) {
            if (this.saldoDisponivel < 0) {
                System.out.println("Seu saldo não está disponível para retirada.");
                return;
            }
            System.out.println("Dite a quantidade de dinheiro que você deseja retirar: ");
            double retirada = scanner.nextDouble();
            if (retirada <= this.saldoDisponivel) {
                System.out.println("Ok enviando o dinheiro...");
                System.out.println("Dinheiro enviado: " + retirada);
                setNewMoney(retirada);
                System.out.println("Seu novo saldo de conta é: " + this.saldoDisponivel);
            }
        } else {
            System.out.println("Digite a quantidade de dinheiro que você deseja inserir: ");
            double quantidadeInserida = scanner.nextDouble();
            setMoneyPlus(quantidadeInserida);
            System.out.println("Seu novo saldo é: " + this.saldoDisponivel);
        }
    }

    public Double getSaldoDisponivel() {
        return this.saldoDisponivel;
    }

    public void menuInicial() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Realizar operações: ");
        System.out.println("1) Retirar dinheiro\n2) Depositar dinheiro\nDigite ao lado: ");
        try {
            int op = scanner.nextInt();
            if (op < 1) {
                System.out.println("Digite um número válido.");
                return;
            }
            retirarDinheiro(op, this.numeroDaConta);
        } catch (Exception e) {
            System.out.println("Digite um número válido.");
        }
    }
}
