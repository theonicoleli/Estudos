import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Pessoa pessoa = new Pessoa();
        ContaBancaria conta = new ContaBancaria();

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu nome: ");
        String nome = scanner.nextLine();
        System.out.println("Digite seu cpf: ");
        String cpf = scanner.nextLine();
        System.out.println("Digite sua idade: ");
        int idade = scanner.nextInt();
        conta.criarSaldo();

        pessoa.adicionarPessoa(nome, cpf, idade);
        pessoa.criarContaBancaria();

        do{
            System.out.printf("Olá %s, seja bem-vindo!\nO número de sua conta bancária é %s\n", pessoa.getNome(), pessoa.getConta());
            conta.verificandoSaldo();
        } while(true);
    }
}
