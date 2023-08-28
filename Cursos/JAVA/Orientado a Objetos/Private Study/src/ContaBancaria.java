import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class ContaBancaria {
    private String nConta;
    private double saldo;

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
        this.nConta = numeroDaConta;
        return this.nConta;
    }

    public void criarSaldo(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o saldo disponível para sua conta: ");
        this.saldo = scanner.nextInt();
    }

    public String getnConta(){
        return this.nConta;
    }

    public void verificandoSaldo(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("1) Retirar dinheiro\n2) Depositar dinheiro");
        System.out.println("Digite a operação a qual você deseja realizar: ");
        try {
            int operacao = scanner.nextInt();
            if (operacao == 1) {
                System.out.println("Digite o valor para retirar: ");
                if (this.saldo < 0) {
                    System.out.println("Você não possui saldo suficiente para esse valor de retirada.");
                    System.out.println("Seu saldo é de: " + this.saldo);
                    return;
                }
                int valorRetirado = scanner.nextInt();
                this.saldo -= valorRetirado;
            }
            else if (operacao == 2) {
                System.out.println("Digite o valor para adicionar: ");
                int valorAdicionado = scanner.nextInt();
                this.saldo += valorAdicionado;
            }
            System.out.println("Seu novo saldo é de: " + this.saldo);
        } catch (Exception e) {
            System.out.println("Digite um valor válido.");
        }
    }
}
